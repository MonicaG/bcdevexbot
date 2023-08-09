import logging
import logging.config
import os

import requests
import tweepy
import yaml

from bcdevexbot import persistence

from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class Twitter:
    """
    Class for interacting with the Tweepy API and formatting twitter statuses.
    """

    HASH_TAG = "#BCDev"
    TWITTER_STATUS_LENGTH = 140
    DEFAULT_TWITTER_URL_LENGTH = 23
    ELLIPSIS = u"\u2026"

    def __init__(self, twitter_credentials, twitter_config_store):
        self._twitter_client = tweepy.Client(
            consumer_key=twitter_credentials['consumer_key'],
            consumer_secret=twitter_credentials['consumer_secret'],
            access_token=twitter_credentials['access_token'],
            access_token_secret=twitter_credentials['access_token_secret'])
        self._twitter_config_store = twitter_config_store
        self._twitter_config = dict()

    def tweet_new_issue(self, url, title):
        status = self._create_status(url, title, "New issue:")
        response = self._twitter_client.create_tweet(text=status)
        logger.info("Tweeted " + status)
        logger.info(f"https://twitter.com/user/status/{response.data['id']}")

    def _create_status(self, url, title, prefix):
        """
        Format the twitter status.  Twitter shortens URL to a specific length,
        so that length must be used in the tweet length calculation rather than
        just getting the length of the status. If the status is too long, then
        it is truncated and ellipsis (...) is used to indicate the truncation
        """
        stripped_prefix = prefix.strip()
        stripped_title = title.strip()
        description = "{0} {1}".format(stripped_prefix, stripped_title)
        formatting_spaces = 2
        url_length = self.get_url_length(url)
        tweet_length = len(description) + url_length + \
            len(Twitter.HASH_TAG) + formatting_spaces
        if tweet_length > Twitter.TWITTER_STATUS_LENGTH:
            over_length = tweet_length - Twitter.TWITTER_STATUS_LENGTH
            description = "{0}{1}".format(description[0:len(description) -
                                          over_length - len(Twitter.ELLIPSIS)],
                                          Twitter.ELLIPSIS)
        status = "{0} {1} {2}".format(description, url, Twitter.HASH_TAG)
        return status

    def get_url_length(self, url):
        """
        Twitter can change the length of its t.co links.  This method gets the
        url length from the configuration store. If it cannot be retrieved
        then a default value is used. See reset_twitter_config method
        """
        url_length = Twitter.DEFAULT_TWITTER_URL_LENGTH
        str_url = str(url).lower()
        if str_url.startswith('http://'):
            url_length = self.get_short_url_length()
        elif str_url.startswith('https://'):
            url_length = self.get_short_url_length_https()
        else:
            logger.warning("Could not determine protocol for url " + url)
        return url_length

    def get_short_url_length(self):
        return self._get_url_length_from_config('short_url_length')

    def get_short_url_length_https(self):
        return self._get_url_length_from_config('short_url_length_https')

    def _get_url_length_from_config(self, key_value):
        self._load_twitter_config()
        url_length = Twitter.DEFAULT_TWITTER_URL_LENGTH
        try:
            url_length = self._twitter_config[key_value]
        except KeyError:
            logger.exception("Could not obtain {0}, using default value"
                             .format(key_value))
        return url_length

    def _load_twitter_config(self):
        """
        Gets the twitter configuration that was stored in the
        reset_twitter_config method
        """
        if len(self._twitter_config) == 0:
            self._twitter_config = self._twitter_config_store.get()

    def reset_twitter_config(self):
        """
        Should only be called once per day.  This gets the twitter
        configuration and stores it. The data includes the url length for
        t.co links.
        See: https://dev.twitter.com/rest/reference/get/help/configuration
        """
        self._twitter_config_store.save(self._api.configuration())


class BCDevExchangeIssues:
    """ Gathers any open opportunities  """

    def __init__(self):
        swu = SprintWithUsOpportunity()
        cwu = CodeWithUsOpportunity()
        twu = TeamWithUsOpportunity()
        self._data = swu.get_opportunities()
        self._data.extend(cwu.get_opportunities())
        self._data.extend(twu.get_opportunities())

    def get_opportunities(self):
        return self._data


class AbstractBCDevExchangeOpportunity(ABC):

    @property
    @abstractmethod
    def api_url(self):
        pass

    @property
    @abstractmethod
    def opportunity_url_base(self):
        pass

    @property
    def status_open(self):
        return "PUBLISHED"

    @property
    def status_closed(self):
        return "AWARDED"

    @property
    def status_evaluation(self):
        return "EVALUATION"

    @property
    def status_eval_questions(self):
        return "EVAL_QUESTIONS"

    @property
    def status_eval_cc(self):
        return "EVAL_CC"

    @property
    def status_eval_scneario(self):
        return "EVAL_SCENARIO"

    @property
    def status_eval_c(self):
        return "EVAL_C"

    def is_status_closed(self, status):
        return status == self.status_closed \
                or status == self.status_evaluation \
                or status == self.status_eval_questions \
                or status == self.status_eval_cc \
                or status == self.status_eval_scneario \
                or status == self.status_eval_c

    def is_status_open(self, status):
        return status == self.status_open

    def _get_url(self, issue_id):
        return self.opportunity_url_base + issue_id

    def get_opportunities(self):
        response = requests.get(self.api_url)
        if response.status_code == requests.codes.ok:
            data = response.json()
            result = []
            for issue in data:
                issue_id, name, status = issue['id'].strip(), \
                    issue['title'].strip(), issue['status'].strip()
                if self.is_status_open(status):
                    result.append((issue_id, self._get_url(issue_id), name))
                elif self.is_status_closed(status):
                    logger.info("Skipping {0} - Closed".format(issue_id))
                else:
                    logger.error("Unknown status {0} for issue {1} - {2}"
                                 .format(status, issue_id, name))
            return result
        else:
            raise ConnectionError(
                "Error connecting to {0}. Status Code: {1} . Reason: {2}"
                .format(self.api_url, response.status_code, response.reason))


class SprintWithUsOpportunity(AbstractBCDevExchangeOpportunity):

    @property
    def api_url(self):
        return 'https://digital.gov.bc.ca/marketplace/api/opportunities/sprint-with-us/'  # noqa: E501

    @property
    def opportunity_url_base(self):
        return 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/'  # noqa: E501


class CodeWithUsOpportunity(AbstractBCDevExchangeOpportunity):

    @property
    def api_url(self):
        return 'https://digital.gov.bc.ca/marketplace/api/opportunities/code-with-us/'  # noqa: E501

    @property
    def opportunity_url_base(self):
        return 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/'  # noqa: E501


class TeamWithUsOpportunity(AbstractBCDevExchangeOpportunity):

    @property
    def api_url(self):
        return 'https://marketplace.digital.gov.bc.ca/api/opportunities/team-with-us/'  # noqa: E501

    @property
    def opportunity_url_base(self):
        return 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/'  # noqa: E501


class Base:
    """Base class for scripts needing to setup Twitter class and logging"""

    def __init__(self, config):
        self.config = config

    def get_twitter(self):
        twitter_config_store = persistence.DataStore(
            self.config['file']['twitter_help_config'])
        return Twitter(self.config['twitter'], twitter_config_store)

    def setup_logging(self):
        path = self.config['file']['logging_config']
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.load(f.read(), Loader=yaml.FullLoader)
            logging.config.dictConfig(config)
        else:
            raise ValueError('Could not find ', path)
