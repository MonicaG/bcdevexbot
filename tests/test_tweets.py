"""
Tests for the bot_tools.Tweet class
"""
from unittest.mock import patch

import pytest
import tweepy

import helpers


@pytest.fixture(scope="module")
@patch('tweepy.API')
def tweet(mock_tweepy):
    tweepy.API()
    tweeter = helpers.Tweet("consumer_key", "consumer_secret", "access_token", "access_token_secret")
    assert mock_tweepy.called
    return tweeter


def test_tweepy_update_status_is_called(tweet):
    tweet.tweet_new_issue("http://example.org", "A title example")
    tweet._api.update_status.assert_called_with("New issue: A title example http://example.org #BCDev")


def test_status_creation_under_max_status_length(tweet):
    status = tweet._create_status('http://example.org', 'A title', 'New Issue: ')

    assert 'New Issue: A title http://example.org #BCDev' == status


def test_status_creation_over_max_status_length(tweet):
    status = tweet._create_status('http://example.org',
                                  '''A very long title that will exceed twitter\'s max length. In order to do this I need to write many, many words.
                                  But that is okay, can just keep typing.''',
                                  'New Issue: '
                                  )

    expected = "New Issue: A very long title that will exceed twitter\'s max length. In order to do this I need to write ma... http://example.org #BCDev"
    assert expected == status


def test_status_creation_equals_max_status_length(tweet):
    url = 'http://example.org/1234'
    assert tweet._TWITTER_DEFINED_URL_LENGTH == len(url)
    status = tweet._create_status(url,
                                  'Here is a title. We need enough characters to make a status exactly'
                                  ' 140 characters long. 1 2 3 4 5',
                                  'New Issue: '
                                  )
    expected = "New Issue: Here is a title. We need enough characters to make a status exactly 140 characters long. 1 2 3 4 5 http://example.org/1234 #BCDev"
    assert expected == status
    assert tweet._TWITTER_STATUS_LENGTH == len(status)


def test_status_creation_1_char_longer_max_status_length(tweet):
    url = 'http://example.org/1234'
    assert tweet._TWITTER_DEFINED_URL_LENGTH == len(url)
    status = tweet._create_status(url,
                                  'Here is a title. We need enough characters to make a status 141 characters long. '
                                  'Extra characters 1',
                                  'New Issue: '
                                  )
    expected = "New Issue: Here is a title. We need enough characters to make a status 141 characters long. Extra characte... http://example.org/1234 #BCDev"

    assert expected == status
    assert tweet._TWITTER_STATUS_LENGTH == len(status)
