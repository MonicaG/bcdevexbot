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
    with open('tests/data/no_issues.json', encoding='utf-8') as cwu_file, \
            open('tests/data/one_issue_swu.json', encoding='utf-8') as swu_file:
        swu = models.SprintWithUsOpportunity()
        cwu = models.CodeWithUsOpportunity()
        data_swu = json.load(swu_file)
        data_cwu = json.load(cwu_file)

        responses.add(responses.GET, swu.api_url,
                      json=data_swu, status=200)
        responses.add(responses.GET, cwu.api_url,
                      json=data_cwu, status=200)

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
    with open('tests/data/no_issues.json', encoding='utf-8') as cwu_file, \
            open('tests/data/one_issue_swu.json', encoding='utf-8') as swu_file:
        swu = models.SprintWithUsOpportunity()
        cwu = models.CodeWithUsOpportunity()
        data_swu = json.load(swu_file)
        data_cwu = json.load(cwu_file)

        responses.add(responses.GET, swu.api_url,
                      json=data_swu, status=200)
        responses.add(responses.GET, cwu.api_url,
                      json=data_cwu, status=200)

        mock_seen_issues.return_value = [100]
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()

        assert mock_seen_issues.called
        mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406'])
        mock_tweet.assert_called_once_with('https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406',
                                           'First Issue')


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_two_issue_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    with open('tests/data/no_issues.json', encoding='utf-8') as cwu_file, \
            open('tests/data/two_issues_swu.json', encoding='utf-8') as swu_file:
        swu = models.SprintWithUsOpportunity()
        cwu = models.CodeWithUsOpportunity()
        data_swu = json.load(swu_file)
        data_cwu = json.load(cwu_file)

        responses.add(responses.GET, swu.api_url,
                      json=data_swu, status=200)
        responses.add(responses.GET, cwu.api_url,
                      json=data_cwu, status=200)

        mock_seen_issues.return_value = [100]
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()

        assert mock_seen_issues.called
        calls = [call('https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406',
                      'First Issue'),
                 call('https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb',
                      'Second Issue')
                 ]
        mock_tweet.assert_has_calls(calls)
        mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406', '58c72cf8aa383e001d84d3fb'])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_two_issue_one_not_seen(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    with open('tests/data/no_issues.json', encoding='utf-8') as cwu_file, \
            open('tests/data/two_issues_swu.json', encoding='utf-8') as swu_file:
        swu = models.SprintWithUsOpportunity()
        cwu = models.CodeWithUsOpportunity()
        data_swu = json.load(swu_file)
        data_cwu = json.load(cwu_file)

        responses.add(responses.GET, swu.api_url,
                      json=data_swu, status=200)
        responses.add(responses.GET, cwu.api_url,
                      json=data_cwu, status=200)

        mock_seen_issues.return_value = ['58c9a3c1aa383e001d84d406']
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()

        assert mock_seen_issues.called
        mock_tweet.assert_called_once_with('https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb',
                                           'Second Issue')
        mock_save_issues.assert_called_once_with(['58c9a3c1aa383e001d84d406', '58c72cf8aa383e001d84d3fb'])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_no_issues(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    with open('tests/data/no_issues.json', encoding='utf-8') as cwu_file, \
            open('tests/data/no_issues.json', encoding='utf-8') as swu_file:
        swu = models.SprintWithUsOpportunity()
        cwu = models.CodeWithUsOpportunity()
        data_swu = json.load(swu_file)
        data_cwu = json.load(cwu_file)

        responses.add(responses.GET, swu.api_url,
                      json=data_swu, status=200)
        responses.add(responses.GET, cwu.api_url,
                      json=data_cwu, status=200)
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
    swu = models.SprintWithUsOpportunity()

    responses.add(responses.GET, swu.api_url,
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
    with open('tests/data/no_issues.json', encoding='utf-8') as cwu_file, \
            open('tests/data/two_issues_swu.json', encoding='utf-8') as swu_file:
        swu = models.SprintWithUsOpportunity()
        cwu = models.CodeWithUsOpportunity()
        data_swu = json.load(swu_file)
        data_cwu = json.load(cwu_file)

        responses.add(responses.GET, swu.api_url,
                      json=data_swu, status=200)
        responses.add(responses.GET, cwu.api_url,
                      json=data_cwu, status=200)



        mock_seen_issues.return_value = []
        mock_tweet.side_effect = tweeting_raises_exception_side_effect
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()

        assert mock_seen_issues.called
        calls = [call('https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406',
                      'First Issue'),
                 call('https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb',
                      'Second Issue')
                 ]
        mock_tweet.assert_has_calls(calls)
        mock_save_issues.assert_called_once_with(['58c72cf8aa383e001d84d3fb'])


def tweeting_raises_exception_side_effect(*args, **kwargs):
    if args[0] == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406':
        raise Exception('Boom')
    else:
        return None


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_only_published_status_are_processed(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    with open('tests/data/three_issues_cwu.json', encoding='utf-8') as cwu_file, \
            open('tests/data/three_issues_swu.json', encoding='utf-8') as swu_file:
        swu = models.SprintWithUsOpportunity()
        cwu = models.CodeWithUsOpportunity()
        data_swu = json.load(swu_file)
        data_cwu = json.load(cwu_file)

        responses.add(responses.GET, swu.api_url,
                      json=data_swu, status=200)
        responses.add(responses.GET, cwu.api_url,
                      json=data_cwu, status=200)

        mock_seen_issues.return_value = ['04003a5f-f609-469f-91bb-f3c6ac56bed7']
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()

        assert mock_seen_issues.called
        calls = [
                call(
                    'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242',
                    'First CWU Issue')
                 ]
        mock_tweet.assert_has_calls(calls)
        mock_save_issues.assert_called_once_with(['04003a5f-f609-469f-91bb-f3c6ac56bed7', 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'])


@responses.activate
@patch('bot.models.Twitter.tweet_new_issue')
@patch('bot.persistence.DataStore.get')
@patch('bot.persistence.DataStore.save')
def test_bad_status_is_not_processed(mock_save_issues, mock_seen_issues, mock_tweet, config_setup):
    with open('tests/data/one_issue_cwu.json', encoding='utf-8') as cwu_file, \
            open('tests/data/unknown_status.json', encoding='utf-8') as unknown_file:
        swu = models.SprintWithUsOpportunity()
        cwu = models.CodeWithUsOpportunity()
        data_swu = json.load(unknown_file)
        data_cwu = json.load(cwu_file)

        responses.add(responses.GET, swu.api_url,
                      json=data_swu, status=200)
        responses.add(responses.GET, cwu.api_url,
                      json=data_cwu, status=200)

        mock_seen_issues.return_value = ['f1f6aca3-7143-41bc-99a7-8ce7014ac242']
        twitter_bot = bot.BCDevExBot(config_setup)
        twitter_bot.process()

        assert mock_seen_issues.called
        calls = []
        mock_tweet.assert_has_calls(calls)
        mock_save_issues.assert_called_once_with(['f1f6aca3-7143-41bc-99a7-8ce7014ac242'])
