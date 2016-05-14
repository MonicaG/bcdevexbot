"""
Test for the new_issues bot.  This makes use of the responses contained in the data.py file.
The id, url and title values contained in the data.py file are used for assertion comparisons in these
tests.
"""
import configparser
from unittest.mock import patch, call

import pytest
import responses

import bot
import tests.data
from bcdevexbot import models

api_url = models.BCDevExchangeIssues._URL


@pytest.fixture(scope="module")
def config_setup():
    config = configparser.ConfigParser()
    config['twitter'] = {'consumer_key': 'ck',
                         'consumer_secret': 'cs',
                         'access_token': 'at',
                         'access_token_secret': 'ats'}
    config['file'] = {'pickle_file': 'issues.pickle',
                      'twitter_help_config': 'twitter_help_config.pickle'}
    return config


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_one_issue_already_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.one_issue, status=200)

    mock_seen_issues.return_value = [101]
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    mock_save_issues.assert_called_once_with([101])
    mock_tweet.assert_not_called()


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_one_issue_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.one_issue, status=200)

    mock_seen_issues.return_value = [100]
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    mock_save_issues.assert_called_once_with([101])
    mock_tweet.assert_called_once_with('https://github.com/bcgov/bc-laws-api/issues/4',
                                       'Favourites Tree Threshold Limit Break')


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_two_issue_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.two_issues, status=200)

    mock_seen_issues.return_value = [100]
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    calls = [call('https://github.com/bcgov/bc-laws-api/issues/4',
                  'Favourites Tree Threshold Limit Break'),
             call('https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7',
                  'Upgrade WP Sage Core Commenting - Part Three - Load More')
             ]
    mock_tweet.assert_has_calls(calls)
    mock_save_issues.assert_called_once_with([101, 102])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_two_issue_one_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.two_issues, status=200)

    mock_seen_issues.return_value = [101]
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    mock_tweet.assert_called_once_with('https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7',
                                       'Upgrade WP Sage Core Commenting - Part Three - Load More')
    mock_save_issues.assert_called_once_with([101, 102])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_no_issues(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.no_issues, status=200)

    mock_seen_issues.return_value = []
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    mock_tweet.assert_not_called
    mock_save_issues.assert_called_once_with([])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_could_not_get_data(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  json={"error": "not found"}, status=404)

    with pytest.raises(ConnectionError):
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()
        mock_seen_issues.assert_not_called
        mock_tweet.assert_not_called
        mock_save_issues.assert_not_called


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_bad_config(mock_save_issues, mock_seen_issues, mock_tweet):
    config = configparser.ConfigParser()
    config['twitter'] = {}
    config['file'] = {'pickle_file': 'issues.pickle', 'twitter_help_config': 'config.pickle'}

    with pytest.raises(KeyError):
        twitter_bot = bot.BCDevExBot(config)
        twitter_bot.process()
        mock_seen_issues.assert_not_called
        mock_tweet.assert_not_called
        mock_save_issues.assert_not_called


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_error_sending_tweet(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    """Test scenario: First issue has an exception while tweeting, second issue tweets successfully
    Expected results: Second issue is processed and its id is stored.  First issue's id is not stored.
    """
    responses.add(responses.GET, api_url,
                  body=tests.data.two_issues, status=200)

    mock_seen_issues.return_value = []
    mock_tweet.side_effect = tweeting_raises_exception_side_effect
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    calls = [call('https://github.com/bcgov/bc-laws-api/issues/4',
                  'Favourites Tree Threshold Limit Break'),
             call('https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7',
                  'Upgrade WP Sage Core Commenting - Part Three - Load More')
             ]
    mock_tweet.assert_has_calls(calls)
    mock_save_issues.assert_called_once_with([102])


def tweeting_raises_exception_side_effect(*args, **kwargs):
    if args[0] == 'https://github.com/bcgov/bc-laws-api/issues/4':
        raise Exception('Boom')
    else:
        return None


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_issue_missing_id(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    """Test scenario: First issue is new and tweeted successfully.  The second issue has bad data (the id is missing)
        Expected results: First issue's id is stored, but second one is not.  Third issue is not processed.
    """
    responses.add(responses.GET, api_url,
                  body=tests.data.missing_id, status=200)

    mock_seen_issues.return_value = []
    with pytest.raises(KeyError):
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()
        assert mock_seen_issues.called
        mock_tweet.assert_called_once_with('https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7',
                                           'Upgrade WP Sage Core Commenting - Part Three - Load More')
        mock_save_issues.assert_called_once_with([101])
