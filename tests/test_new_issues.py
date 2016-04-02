"""
Test for the new_issues bot.  This makes use of the responses contained in the data.py file.
The id, url and title values contained in the data.py file are used for assertion comparisons in these
tests.
"""
from bcdevexbot import bot_tools
from bcdevexbot import new_issues
import responses
import pytest
import tests.data
from unittest.mock import patch, call
import configparser

api_url = bot_tools.BCDevExchangeIssues._URL


@pytest.fixture(scope="module")
def config_setup():
    config = configparser.ConfigParser()
    config['twitter'] = {'consumer_key': 'ck',
                         'consumer_secret': 'cs',
                         'access_token': 'at',
                         'access_token_secret': 'ats'}
    config['file'] = {'pickle_file': 'issues.pickle'}
    return config


@responses.activate
@patch('bcdevexbot.new_issues.Tweet.tweet_new_issue')
@patch('bcdevexbot.new_issues.StoredIssues.get_seen_issues')
@patch('bcdevexbot.new_issues.StoredIssues.save_issues')
def test_one_issue_already_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.one_issue, status=200)

    mock_seen_issues.return_value = [101]
    new_issues.process(config_setup)

    assert mock_seen_issues.called
    mock_save_issues.assert_called_once_with([101])
    mock_tweet.assert_not_called()


@responses.activate
@patch('bcdevexbot.new_issues.Tweet.tweet_new_issue')
@patch('bcdevexbot.new_issues.StoredIssues.get_seen_issues')
@patch('bcdevexbot.new_issues.StoredIssues.save_issues')
def test_one_issue_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.one_issue, status=200)

    mock_seen_issues.return_value = [100]
    new_issues.process(config_setup)

    assert mock_seen_issues.called
    mock_save_issues.assert_called_once_with([101])
    mock_tweet.assert_called_once_with('https://github.com/bcgov/bc-laws-api/issues/4',
                                       'Favourites Tree Threshold Limit Break')


@responses.activate
@patch('bcdevexbot.new_issues.Tweet.tweet_new_issue')
@patch('bcdevexbot.new_issues.StoredIssues.get_seen_issues')
@patch('bcdevexbot.new_issues.StoredIssues.save_issues')
def test_two_issue_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.two_issues, status=200)

    mock_seen_issues.return_value = [100]
    new_issues.process(config_setup)

    assert mock_seen_issues.called
    calls = [call('https://github.com/bcgov/bc-laws-api/issues/4',
                  'Favourites Tree Threshold Limit Break'),
             call('https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7',
                  'Upgrade WP Sage Core Commenting - Part Three - Load More')
             ]
    mock_tweet.assert_has_calls(calls)
    mock_save_issues.assert_called_once_with([101, 102])


@responses.activate
@patch('bcdevexbot.new_issues.Tweet.tweet_new_issue')
@patch('bcdevexbot.new_issues.StoredIssues.get_seen_issues')
@patch('bcdevexbot.new_issues.StoredIssues.save_issues')
def test_two_issue_one_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.two_issues, status=200)

    mock_seen_issues.return_value = [101]
    new_issues.process(config_setup)

    assert mock_seen_issues.called
    mock_tweet.assert_called_once_with('https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7',
                                       'Upgrade WP Sage Core Commenting - Part Three - Load More')
    mock_save_issues.assert_called_once_with([101, 102])


@responses.activate
@patch('bcdevexbot.new_issues.Tweet.tweet_new_issue')
@patch('bcdevexbot.new_issues.StoredIssues.get_seen_issues')
@patch('bcdevexbot.new_issues.StoredIssues.save_issues')
def test_no_issues(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  body=tests.data.no_issues, status=200)

    mock_seen_issues.return_value = []
    new_issues.process(config_setup)

    assert mock_seen_issues.called
    mock_tweet.assert_not_called
    mock_save_issues.assert_called_once_with([])


@responses.activate
@patch('bcdevexbot.new_issues.Tweet.tweet_new_issue')
@patch('bcdevexbot.new_issues.StoredIssues.get_seen_issues')
@patch('bcdevexbot.new_issues.StoredIssues.save_issues')
def test_could_not_get_data(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    responses.add(responses.GET, api_url,
                  json={"error": "not found"}, status=404)

    with pytest.raises(ConnectionError):
        new_issues.process(config_setup)
        mock_seen_issues.assert_not_called
        mock_tweet.assert_not_called
        mock_save_issues.assert_not_called


@responses.activate
@patch('bcdevexbot.new_issues.Tweet.tweet_new_issue')
@patch('bcdevexbot.new_issues.StoredIssues.get_seen_issues')
@patch('bcdevexbot.new_issues.StoredIssues.save_issues')
def test_bad_config(mock_save_issues, mock_seen_issues, mock_tweet):
    config = configparser.ConfigParser()
    config['twitter'] = {}
    config['file'] = {'pickle_file': 'issues.pickle'}

    with pytest.raises(KeyError):
        new_issues.process(config)
        mock_seen_issues.assert_not_called
        mock_tweet.assert_not_called
        mock_save_issues.assert_not_called