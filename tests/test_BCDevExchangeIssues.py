""" Test the BCDevExchangeIssues class """

import pytest
import responses

import tests.data
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
    responses.add(responses.GET, api_url,
                  body=tests.data.no_issues, status=200)
    open_issues = models.BCDevExchangeIssues()
    with pytest.raises(StopIteration):
        open_issues.__next__()


@responses.activate
def test_one_issue():
    responses.add(responses.GET, api_url,
                  body=tests.data.one_issue, status=200)
    open_issues = models.BCDevExchangeIssues()
    issue_id, url, title = open_issues.__next__()
    assert issue_id == '58c9a3c1aa383e001d84d406'
    assert url == 'https://bcdevexchange.org/opportunities/first-issue'
    assert title == 'First Issue'

    with pytest.raises(StopIteration):
        open_issues.__next__()


@responses.activate
def test_two_issues():
    responses.add(responses.GET, api_url,
                  body=tests.data.two_issues, status=200)
    open_issues = models.BCDevExchangeIssues()
    issue_id, url, title = open_issues.__next__()
    assert issue_id == '58c9a3c1aa383e001d84d406'
    assert url == 'https://bcdevexchange.org/opportunities/first-issue'
    assert title == 'First Issue'

    issue_id, url, title = open_issues.__next__()
    assert issue_id == '58c72cf8aa383e001d84d3fb'
    assert url == 'https://bcdevexchange.org/opportunities/second-issue'
    assert title == 'Second Issue'

    with pytest.raises(StopIteration):
        open_issues.__next__()


@responses.activate
def test_empty_code():
    responses.add(responses.GET, api_url, body=tests.data.empty_code, status=200)
    open_issues = models.BCDevExchangeIssues()
    issue_id, url, title = open_issues.__next__()
    assert issue_id == '58c9a3c1aa383e001d84d406'
    assert url == 'https://github.com/bcgov/first-issue'
    assert title == 'First Issue'


@responses.activate
def test_code_starts_with_slash():
    responses.add(responses.GET, api_url,
                  body=tests.data.code_starts_with_slash, status=200)
    open_issues = models.BCDevExchangeIssues()
    issue_id, url, title = open_issues.__next__()
    assert issue_id == '58c9a3c1aa383e001d84d406'
    assert url == 'https://bcdevexchange.org/opportunities/first-issue'
    assert title == 'First Issue'

    with pytest.raises(StopIteration):
        open_issues.__next__()


