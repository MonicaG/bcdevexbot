"""
Test for the new_issues bot.  Uses the json files in the data directory.
The id, url and title values contained in the various json files are used for assertion comparisons in these
tests.
"""
import configparser
from unittest.mock import patch, call

import pytest
import responses
import json

import bot
from bcdevexbot import models

api_url = models.BCDevExchangeIssues.URL


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
    data = json.load(open('data/one_issue.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)

    mock_seen_issues.return_value = ['58c9a3c1aa383e001d84d406']
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406'])
    mock_tweet.assert_not_called()


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_one_issue_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    data = json.load(open('data/one_issue.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)

    mock_seen_issues.return_value = [100]
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406'])
    mock_tweet.assert_called_once_with('https://bcdevexchange.org/opportunities/swu/first-issue',
                                       'First Issue')


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_two_issue_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    data = json.load(open('data/two_issues.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)

    mock_seen_issues.return_value = [100]
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    calls = [call('https://bcdevexchange.org/opportunities/swu/first-issue',
                  'First Issue'),
             call('https://bcdevexchange.org/opportunities/cwu/second-issue',
                  'Second Issue')
             ]
    mock_tweet.assert_has_calls(calls)
    mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406', '58c72cf8aa383e001d84d3fb'])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_two_issue_one_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    data = json.load(open('data/two_issues.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)

    mock_seen_issues.return_value = ['58c9a3c1aa383e001d84d406']
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    mock_tweet.assert_called_once_with('https://bcdevexchange.org/opportunities/cwu/second-issue',
                                       'Second Issue')
    mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406', '58c72cf8aa383e001d84d3fb'])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_no_issues(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    data = json.load(open('data/no_issues.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)

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
    data = json.load(open('data/two_issues.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)

    mock_seen_issues.return_value = []
    mock_tweet.side_effect = tweeting_raises_exception_side_effect
    twitter_bot = bot.BCDevExBot(config_setup)
    twitter_bot.process()

    assert mock_seen_issues.called
    calls = [call('https://bcdevexchange.org/opportunities/swu/first-issue',
                  'First Issue'),
             call('https://bcdevexchange.org/opportunities/cwu/second-issue',
                  'Second Issue')
             ]
    mock_tweet.assert_has_calls(calls)
    mock_save_issues.assert_called_once_with(['58c72cf8aa383e001d84d3fb'])


def tweeting_raises_exception_side_effect(*args, **kwargs):
    if args[0] == 'https://bcdevexchange.org/opportunities/swu/first-issue':
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
    data = json.load(open('data/missing_id.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)

    with pytest.raises(KeyError):
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()
    assert mock_seen_issues.called
    mock_tweet.assert_called_once_with('https://bcdevexchange.org/opportunities/swu/first-issue', 'First Issue')
    mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406'])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_unknown_opportunity_type(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    """Test scenario: First issue is new and tweeted successfully The second issue has an unknown opportunity type.
        Expected results: First issue's id is stored, but second one is not. The third issue is not processed.
    """
    data = json.load(open('data/unknown_opportunity_type.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)

    mock_seen_issues.return_value = []
    with pytest.raises(ValueError):
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()
    assert mock_seen_issues.called
    mock_tweet.assert_called_once_with('https://bcdevexchange.org/opportunities/swu/first-issue', 'First Issue')
    mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406'])
