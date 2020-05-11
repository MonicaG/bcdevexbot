""" Test the BCDevExchangeIssues class """
import unittest
import responses
import json

from bcdevexbot import models


class BCDevExchangeIssuesTests(unittest.TestCase):

    @responses.activate
    def test_no_issues(self):
        with open('tests/data/no_issues.json', encoding='utf-8') as file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            data = json.load(file)
            responses.add(responses.GET, swu.api_url,
                          json=data, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data, status=200)
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 0

    @responses.activate
    def test_one_swu_issue_no_cwu_issues(self):
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
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 1
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'
            assert title == 'First Issue'

    @responses.activate
    def test_two_swu_issue_no_cwu_issues(self):
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
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 2
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'
            assert title == 'First Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == '58c72cf8aa383e001d84d3fb'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb'
            assert title == 'Second Issue'

    @responses.activate
    def test_two_swu_issue_one_cwu_issues(self):
        with open('tests/data/one_issue_cwu.json', encoding='utf-8') as cwu_file, \
                open('tests/data/two_issues_swu.json', encoding='utf-8') as swu_file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 3
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'
            assert title == 'First Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == '58c72cf8aa383e001d84d3fb'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb'
            assert title == 'Second Issue'

            issue_id, url, title = open_issues[2]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert title == 'First CWU Issue'

    @responses.activate
    def test_two_swu_issue_two_cwu_issues(self):
        with open('tests/data/two_issues_cwu.json', encoding='utf-8') as cwu_file, \
                open('tests/data/two_issues_swu.json', encoding='utf-8') as swu_file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 4
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'
            assert title == 'First Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == '58c72cf8aa383e001d84d3fb'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb'
            assert title == 'Second Issue'

            issue_id, url, title = open_issues[2]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert title == 'First CWU Issue'

            issue_id, url, title = open_issues[3]
            assert issue_id == 'd2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/d2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert title == 'Second CWU Issue'

    @responses.activate
    def test_one_swu_issue_two_cwu_issues(self):
        with open('tests/data/two_issues_cwu.json', encoding='utf-8') as cwu_file, \
                open('tests/data/one_issue_swu.json', encoding='utf-8') as swu_file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 3
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'
            assert title == 'First Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert title == 'First CWU Issue'

            issue_id, url, title = open_issues[2]
            assert issue_id == 'd2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/d2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert title == 'Second CWU Issue'

    @responses.activate
    def test_no_swu_issue_two_cwu_issues(self):
        with open('tests/data/two_issues_cwu.json', encoding='utf-8') as cwu_file, \
                open('tests/data/no_issues.json', encoding='utf-8') as swu_file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 2

            issue_id, url, title = open_issues[0]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert title == 'First CWU Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == 'd2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/d2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert title == 'Second CWU Issue'


if __name__ == '__main__':
    unittest.main()
