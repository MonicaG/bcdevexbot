""" Test the BCDevExchangeIssues class """

import pytest
import responses
import json

from bcdevexbot import models

api_url = models.BCDevExchangeIssues.URL

@responses.activate
def test_connection_issue():
    responses.add(responses.GET, api_url,
                  json={"error": "not found"}, status=404)

    with pytest.raises(ConnectionError):
        models.BCDevExchangeIssues()


@responses.activate
def test_no_issues():
    data = json.load(open('tests/data/no_issues.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)
    open_issues = models.BCDevExchangeIssues()
    with pytest.raises(StopIteration):
        open_issues.__next__()


@responses.activate
def test_one_issue():
    data = json.load(open('tests/data/one_issue.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)
    open_issues = models.BCDevExchangeIssues()
    issue_id, url, title = open_issues.__next__()
    assert issue_id == '58c9a3c1aa383e001d84d406'
    assert url == 'https://bcdevexchange.org/opportunities/swu/first-issue'
    assert title == 'First Issue'

    with pytest.raises(StopIteration):
        open_issues.__next__()


@responses.activate
def test_two_issues():
    data = json.load(open('tests/data/two_issues.json', encoding='utf-8'))
    responses.add(responses.GET, api_url,
                  json=data, status=200)
    open_issues = models.BCDevExchangeIssues()
    issue_id, url, title = open_issues.__next__()
    assert issue_id == '58c9a3c1aa383e001d84d406'
    assert url == 'https://bcdevexchange.org/opportunities/swu/first-issue'
    assert title == 'First Issue'

    issue_id, url, title = open_issues.__next__()
    assert issue_id == '58c72cf8aa383e001d84d3fb'
    assert url == 'https://bcdevexchange.org/opportunities/cwu/second-issue'
    assert title == 'Second Issue'

    with pytest.raises(StopIteration):
        open_issues.__next__()


@responses.activate
def test_empty_code():
    data = json.load(open('tests/data/empty_code.json', encoding='utf-8'))

    responses.add(responses.GET, api_url, json=data, status=200)
    open_issues = models.BCDevExchangeIssues()
    issue_id, url, title = open_issues.__next__()
    assert issue_id == '5c1438ba4dd91200190627af'
    assert url == 'https://github.com/bcgov/first-issue'
    assert title == 'First Issue'


def test_code_starts_with_slash():
    expected_link = 'https://bcdevexchange.org/opportunities/swu/first-issue'
    actual_link = models.BCDevExchangeIssues.get_url('/first-issue',
                                                     'https://github.com/bcgov/databc-web-map-services/issues/3',
                                                     'sprint-with-us')
    assert expected_link == actual_link


def test_get_opportunity_type_code_swu():
    expected_link = "https://bcdevexchange.org/opportunities/swu/opp-industrial-ghg-reporting-database-improvements"
    actual_link = models.BCDevExchangeIssues.get_url("opp-industrial-ghg-reporting-database-improvements",
                                    "https://github.com/Maralsotoudehnia/CAS-Industrial-GHG-System-Improvements/",
                                    "sprint-with-us")
    assert expected_link == actual_link


def test_get_opportunity_type_code_cwu():
    expected_link = 'https://bcdevexchange.org/opportunities/cwu/opp-create-sprint-with-us--code-challenge'
    actual_link = models.BCDevExchangeIssues.get_url('opp-create-sprint-with-us--code-challenge',
                                                     'github.com/BCDevExchange-CodeChallenge/CodeChallengeRules/',
                                                     'code-with-us')
    assert expected_link == actual_link


def test_get_opportunity_type_code_unknown_code():
    with pytest.raises(ValueError):
        models.BCDevExchangeIssues.get_url('opp-create-sprint-with-us--code-challenge',
                                           'github.com/BCDevExchange-CodeChallenge/CodeChallengeRules/',
                                           'unknown')
