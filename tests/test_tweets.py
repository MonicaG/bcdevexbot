""" Tests for the Twitter class """

from unittest.mock import patch

import pytest
import tweepy

from bcdevexbot import models, persistence

URL_LENGTH = 20
TWITTER_CONFIG = {'short_url_length': URL_LENGTH,
                  'short_url_length_https': URL_LENGTH}


@pytest.fixture
@patch('tweepy.Client')
def tweet(mock_tweepy):
    tweepy.Client()

    credentials = {'consumer_key': 'consumer_key',
                   'consumer_secret': 'consumer_secret',
                   'access_token': 'access_token',
                   'access_token_secret': 'access_token_secret'
                   }

    tweeter = models.Twitter(credentials,
                             persistence.DataStore('/path/to/file'))
    assert mock_tweepy.called

    return tweeter


@patch('bcdevexbot.persistence.DataStore.get')
def test_tweepy_update_status_is_called(mock_twitter_config, tweet):
    mock_twitter_config.return_value = TWITTER_CONFIG
    tweet.tweet_new_issue("http://example.org", "A title example")
    tweet._twitter_client.create_tweet.assert_called_with(
        text="New issue: A title example http://example.org #BCDev")
    mock_twitter_config.assert_called_once_with()


@patch('bcdevexbot.persistence.DataStore.get')
def test_status_creation_under_max_status_length(mock_twitter_config, tweet):
    mock_twitter_config.return_value = TWITTER_CONFIG
    status = tweet._create_status(
        'http://example.org', 'A title', 'New Issue: ')
    assert 'New Issue: A title http://example.org #BCDev' == status
    mock_twitter_config.assert_called_once_with()


@patch('bcdevexbot.persistence.DataStore.get')
def test_status_creation_over_max_status_length(mock_twitter_config, tweet, ):
    url = 'http://example.org/1'
    # make the url length the same length as used in the tweet composition
    # calculation.  This is just a hack for this test so we can use the
    # len(status) test below and have it equal the correct amount. So, I've
    # magically made the url to be the same length as the config url length
    # value.
    assert URL_LENGTH == len(url)
    mock_twitter_config.return_value = TWITTER_CONFIG
    title = ('A very long title that will exceed twitter\'s max length. '
             'In order to do this I need to write many, many words. But that '
             'is okay, can just keep typing.')

    status = tweet._create_status(url,
                                  title,
                                  'New Issue: '
                                  )

    assert tweet.TWITTER_STATUS_LENGTH == len(status)
    expected = ('New Issue: A very long title that will exceed twitter\'s max '
                'length. In order to do this I need to write many, '
                'm\u2026 http://example.org/1 #BCDev')
    assert expected == status
    mock_twitter_config.assert_called_once_with()


@patch('bcdevexbot.persistence.DataStore.get')
def test_status_creation_equals_max_status_length(mock_twitter_config, tweet):
    url = 'http://example.org/1'
    # see comment in above test on why url length needs to be a certain length
    assert URL_LENGTH == len(url)
    mock_twitter_config.return_value = TWITTER_CONFIG
    status = tweet._create_status(url,
                                  'Here is a title. We need enough characters to make a status exactly 140 characters '  # noqa: E501
                                  'long. 1234567890ab',
                                  'New Issue: '
                                  )
    expected = ('New Issue: Here is a title. We need enough characters to make a status exactly 140 characters '  # noqa: E501
                'long. 1234567890ab http://example.org/1 #BCDev')
    assert expected == status
    assert tweet.TWITTER_STATUS_LENGTH == len(status)
    mock_twitter_config.assert_called_once_with()


@patch('bcdevexbot.persistence.DataStore.get')
def test_status_creation_1_char_longer_max_status_length(
        mock_twitter_config, tweet):
    url = 'http://example.org/1'
    # see comment in above test on why url length needs to be a certain length
    assert URL_LENGTH == len(url)
    mock_twitter_config.return_value = TWITTER_CONFIG
    status = tweet._create_status(url,
                                  'Here is a title. We need enough characters to make a status 141 characters long. '  # noqa: E501
                                  'Extra characters 1234',
                                  'New Issue: '
                                  )
    expected = ('New Issue: Here is a title. We need enough characters to make'
                ' a status 141 characters long. '
                'Extra characters 12\u2026 http://example.org/1 #BCDev')

    assert tweet.TWITTER_STATUS_LENGTH == len(status)
    assert expected == status
    mock_twitter_config.assert_called_once_with()


@patch('bcdevexbot.persistence.DataStore.get')
def test_multiple_calls_to_update_status(mock_twitter_config, tweet):
    mock_twitter_config.return_value = TWITTER_CONFIG
    tweet.tweet_new_issue("http://example.org", "A title example")
    tweet._twitter_client.create_tweet.assert_called_with(
       text="New issue: A title example http://example.org #BCDev")
    tweet.tweet_new_issue("http://example2.org", "Title 2 example")
    tweet._twitter_client.create_tweet.assert_called_with(
        text="New issue: Title 2 example http://example2.org #BCDev")
    mock_twitter_config.assert_called_once_with()


@patch('bcdevexbot.persistence.DataStore.get')
def test_url_length_config_not_found(mock_twitter_config, tweet):
    mock_twitter_config.return_value = {}
    assert tweet.DEFAULT_TWITTER_URL_LENGTH == tweet.get_short_url_length()


@patch('bcdevexbot.persistence.DataStore.get')
def test_https_link(mock_twitter_config, tweet):
    mock_twitter_config.return_value = TWITTER_CONFIG
    tweet.tweet_new_issue("https://example.org", "A title example")
    tweet._twitter_client.create_tweet.assert_called_with(
        text="New issue: A title example https://example.org #BCDev")
    mock_twitter_config.assert_called_once_with()


@patch('bcdevexbot.persistence.DataStore.get')
def test_missing_protocol_link(mock_twitter_config, tweet):
    mock_twitter_config.return_value = TWITTER_CONFIG
    url_length = tweet.get_url_length("www.example.com")
    assert tweet.DEFAULT_TWITTER_URL_LENGTH == url_length


@patch('bcdevexbot.persistence.DataStore.get')
def test_get_url_length(mock_twitter_config, tweet):
    mock_twitter_config.return_value = TWITTER_CONFIG
    url_length = tweet.get_url_length("http://example.com")
    assert URL_LENGTH == url_length
