import pickle
import requests
import tweepy
import logging

logger = logging.getLogger()


class StoredIssues:
    """
    Persists and retrieves issue_ids.  A issue_id is the "{issues : [ ... "id" : value ... ] }" from the
    BC Developers API response.
    """

    def __init__(self, file_name):
        self._file_name = file_name

    def save_issues(self, issue_ids):
        """Persist a Lis of issue_ids"""
        with open(self._file_name, 'wb') as f:
            pickle.dump(issue_ids, f)

    def get_seen_issues(self):
        """Returns a List of issue_ids"""
        try:
            with open(self._file_name, 'rb') as f:
                seen_issues = pickle.load(f)
        except FileNotFoundError:
            logger.debug("Could not find file ", self._file_name)
            seen_issues = ()
        return seen_issues


class Tweet:
    """
    Class for interacting with the Tweepy API and formatting twitter statuses.
    """

    _HASH_TAG = "#BCDev"
    _TWITTER_STATUS_LENGTH = 140
    _TWITTER_DEFINED_URL_LENGTH = 23
    _ELLIPSIS = "..."

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self._api = tweepy.API(auth)

    def tweet_new_issue(self, url, title):
        status = self._create_status(url, title, "New issue:")
        self._api.update_status(status)

    def _create_status(self, url, title, prefix):
        """
        Format the twitter status.  Twitter shortens URL to a specific length, so that length must be used
        in the tweet length calculation rather than just getting the length of the status.
        If the status is too long, then it is truncated and ellipsis (...) is used to indicate the truncation
        """
        stripped_prefix = prefix.strip()
        stripped_title = title.strip()
        description = "{0} {1}".format(stripped_prefix, stripped_title)
        formatting_spaces = 2
        tweet_length = len(description) + Tweet._TWITTER_DEFINED_URL_LENGTH + len(Tweet._HASH_TAG) + formatting_spaces
        if tweet_length > Tweet._TWITTER_STATUS_LENGTH:
            over_length = tweet_length - Tweet._TWITTER_STATUS_LENGTH
            description = "{0} {1}{2}".format(stripped_prefix,
                                              stripped_title[
                                              0:len(stripped_title) - over_length - len(Tweet._ELLIPSIS)],
                                              Tweet._ELLIPSIS)
        status = "{0} {1} {2}".format(description, url, Tweet._HASH_TAG)
        logger.info(status)
        return status


class BCDevExchangeIssues:
    """
    Class for interacting with the BC Developer Exchange API
    """

    _URL = 'https://bcdevexchange.org/api/issues'

    def __init__(self):
        response = requests.get(BCDevExchangeIssues._URL)
        if response.status_code == requests.codes.ok:
            self.data = response.json()['issues']
            self.index = 0
        else:
            raise ConnectionError(
                "Error connecting. Status Code: {0} . Reason: {1}".format(response.status_code, response.reason))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        issue = self.data[self.index]
        self.index += 1
        return issue['id'], issue['html_url'], issue['title']
