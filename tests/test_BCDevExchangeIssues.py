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
    assert issue_id == 101
    assert url == 'https://github.com/bcgov/first-issue'
    assert title == 'First Issue'

    with pytest.raises(StopIteration):
        open_issues.__next__()


@responses.activate
def test_two_issues():
    responses.add(responses.GET, api_url,
                  body=tests.data.two_issues, status=200)
    open_issues = models.BCDevExchangeIssues()
    issue_id, url, title = open_issues.__next__()
    assert issue_id == 101
    assert url == 'https://github.com/bcgov/first-issue'
    assert title == 'First Issue'

    issue_id, url, title = open_issues.__next__()
    assert issue_id == 102
    assert url == 'https://github.com/bcgov/second-issue'
    assert title == 'Second Issue'

    with pytest.raises(StopIteration):
        open_issues.__next__()



