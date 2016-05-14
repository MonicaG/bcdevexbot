import logging
import logging.config
import os

import requests
import tweepy
import yaml

from bcdevexbot import persistence

logger = logging.getLogger(__name__)


class Twitter:
    """ Class for interacting with the Tweepy API and formatting twitter statuses. """

    _HASH_TAG = "#BCDev"
    _TWITTER_STATUS_LENGTH = 140
    _DEFAULT_TWITTER_URL_LENGTH = 23
    _ELLIPSIS = "..."

    def __init__(self, twitter_credentials, twitter_config_store):
        auth = tweepy.OAuthHandler(twitter_credentials['consumer_key'], twitter_credentials['consumer_secret'])
        auth.set_access_token(twitter_credentials['access_token'], twitter_credentials['access_token_secret'])
        self._api = tweepy.API(auth)
        self._twitter_config_store = twitter_config_store
        self._twitter_config = dict()

    def tweet_new_issue(self, url, title):
        status = self._create_status(url, title, "New issue:")
        self._api.update_status(status)
        logger.info("Tweeted " + status)

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
        url_length = self.get_url_length(url)
        tweet_length = len(description) + url_length + len(Twitter._HASH_TAG) + formatting_spaces
        if tweet_length > Twitter._TWITTER_STATUS_LENGTH:
            over_length = tweet_length - Twitter._TWITTER_STATUS_LENGTH
            description = "{0} {1}{2}".format(stripped_prefix,
                                              stripped_title[
                                              0:len(stripped_title) - over_length - len(Twitter._ELLIPSIS)],
                                              Twitter._ELLIPSIS)
        status = "{0} {1} {2}".format(description, url, Twitter._HASH_TAG)
        return status

    def get_url_length(self, url):
        """
        Twitter can change the length of its t.co links.  This method gets the url length from the configuration store.
        If it cannot be retrieved then a default value is used.
        See reset_twitter_config method
        """
        url_length = Twitter._DEFAULT_TWITTER_URL_LENGTH
        str_url = str(url).lower()
        if str_url.startswith('http://'):
            url_length = self.get_short_url_length()
        elif str_url.startswith('https://'):
            url_length = self.get_short_url_length_https()
        else:
            logger.warn("Could not determine protocol for url " + url)
        return url_length

    def get_short_url_length(self):
        return self._get_url_length_from_config('short_url_length')

    def get_short_url_length_https(self):
        return self._get_url_length_from_config('short_url_length_https')

    def _get_url_length_from_config(self, key_value):
        self._load_twitter_config()
        url_length = Twitter._DEFAULT_TWITTER_URL_LENGTH
        try:
            url_length = self._twitter_config[key_value]
        except KeyError:
            logger.exception("Could not obtain {0}, using default value".format(key_value))
        return url_length

    def _load_twitter_config(self):
        """Gets the twitter configuration that was stored in the reset_twitter_config method"""
        if len(self._twitter_config) == 0:
            self._twitter_config = self._twitter_config_store.get()

    def reset_twitter_config(self):
        """
        Should only be called once per day.  This gets the twitter configuration and stores it.
        The data includes the url length for t.co links.
        See: https://dev.twitter.com/rest/reference/get/help/configuration
        """
        self._twitter_config_store.save(self._api.configuration())


class BCDevExchangeIssues:
    """ Class for interacting with the BC Developer Exchange API """

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


class Base:
    """Base class for scripts needing to setup Twitter class and logging"""
    def __init__(self, config):
        self.config = config

    def get_twitter(self):
        twitter_config_store = persistence.DataStore(self.config['file']['twitter_help_config'])
        return Twitter(self.config['twitter'], twitter_config_store)

    def setup_logging(self):
        path = self.config['file']['logging_config']
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.load(f.read())
            logging.config.dictConfig(config)
        else:
            raise ValueError('Could not find ', path)
