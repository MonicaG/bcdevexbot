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
            twu = models.TeamWithUsOpportunity()
            data = json.load(file)
            responses.add(responses.GET, swu.api_url,
                          json=data, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data, status=200)

            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 0

    @responses.activate
    def test_one_swu_issue_no_cwu_issues_no_twu_issue(self):
        with open('tests/data/no_issues.json', encoding='utf-8') \
                as empty_file, \
                open('tests/data/one_issue_swu.json', encoding='utf-8') \
                as swu_file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_empty = json.load(empty_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_empty, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data_empty, status=200)
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 1
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'  # noqa: E501
            assert title == 'First Issue'

    @responses.activate
    def test_two_swu_issue_no_cwu_issues_no_twu_issues(self):
        with open('tests/data/no_issues.json', encoding='utf-8') \
            as empty_file, \
                open('tests/data/two_issues_swu.json', encoding='utf-8') \
                as swu_file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_empty = json.load(empty_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_empty, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data_empty, status=200)
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 2
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'  # noqa: E501
            assert title == 'First Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == '58c72cf8aa383e001d84d3fb'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb'  # noqa: E501
            assert title == 'Second Issue'

    @responses.activate
    def test_two_swu_issue_one_cwu_issues_one_twu_issue(self):
        with open('tests/data/one_issue_cwu.json', encoding='utf-8') \
                as cwu_file, \
                open('tests/data/two_issues_swu.json', encoding='utf-8') \
                as swu_file, \
                open('tests/data/one_issue_twu.json', encoding='utf-8') \
                as twu_file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)
            data_twu = json.load(twu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data_twu, status=200)

            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 4
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'  # noqa: E501
            assert title == 'First Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == '58c72cf8aa383e001d84d3fb'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb'  # noqa: E501
            assert title == 'Second Issue'

            issue_id, url, title = open_issues[2]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'  # noqa: E501
            assert title == 'First CWU Issue'

            issue_id, url, title = open_issues[3]
            assert issue_id == 'ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'
            assert url == 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'  # noqa: E501
            assert title == 'First TWU Issue'

    @responses.activate
    def test_two_swu_issue_two_cwu_issues_two_twu_issues(_self):
        with open('tests/data/two_issues_cwu.json', encoding='utf-8') \
                as cwu_file, \
                open('tests/data/two_issues_swu.json', encoding='utf-8') \
                as swu_file, \
                open('tests/data/two_issues_twu.json', encoding='utf-8') \
                as twu_file:

            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)
            data_twu = json.load(twu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data_twu, status=200)

            open_issues = models.BCDevExchangeIssues().get_opportunities()

            assert len(open_issues) == 6
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'  # noqa: E501
            assert title == 'First Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == '58c72cf8aa383e001d84d3fb'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c72cf8aa383e001d84d3fb'  # noqa: E501
            assert title == 'Second Issue'

            issue_id, url, title = open_issues[2]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'  # noqa: E501
            assert title == 'First CWU Issue'

            issue_id, url, title = open_issues[3]
            assert issue_id == 'd2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/d2a6aca3-7143-41bc-99a7-8ce7014ac3af'  # noqa: E501
            assert title == 'Second CWU Issue'

            issue_id, url, title = open_issues[4]
            assert issue_id == 'ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'
            assert url == 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'  # noqa: E501
            assert title == 'First TWU Issue'

            issue_id, url, title = open_issues[5]
            assert issue_id == 'd111be71-bd4b-8893-ab41-3c9143ae445b'
            assert url == 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/d111be71-bd4b-8893-ab41-3c9143ae445b'  # noqa: E501
            assert title == 'Second TWU Issue'

    @responses.activate
    def test_one_swu_issue_two_cwu_issues_two_twu_issues(self):
        with open('tests/data/two_issues_cwu.json', encoding='utf-8') \
                as cwu_file, \
                open('tests/data/one_issue_swu.json', encoding='utf-8') \
                as swu_file, \
                open('tests/data/two_issues_twu.json', encoding='utf-8') \
                as twu_file:

            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)
            data_twu = json.load(twu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data_twu, status=200)

            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 5
            issue_id, url, title = open_issues[0]
            assert issue_id == '58c9a3c1aa383e001d84d406'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/58c9a3c1aa383e001d84d406'  # noqa: E501
            assert title == 'First Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'  # noqa: E501
            assert title == 'First CWU Issue'

            issue_id, url, title = open_issues[2]
            assert issue_id == 'd2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/d2a6aca3-7143-41bc-99a7-8ce7014ac3af'  # noqa: E501
            assert title == 'Second CWU Issue'

            issue_id, url, title = open_issues[3]
            assert issue_id == 'ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'
            assert url == 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'  # noqa: E501
            assert title == 'First TWU Issue'

            issue_id, url, title = open_issues[4]
            assert issue_id == 'd111be71-bd4b-8893-ab41-3c9143ae445b'
            assert url == 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/d111be71-bd4b-8893-ab41-3c9143ae445b'  # noqa: E501
            assert title == 'Second TWU Issue'

    @responses.activate
    def test_no_swu_issue_two_cwu_issues_one_twu_issue(self):
        with open('tests/data/two_issues_cwu.json', encoding='utf-8') \
                as cwu_file, \
                open('tests/data/no_issues.json', encoding='utf-8') \
                as swu_file, \
                open('tests/data/one_issue_twu.json', encoding='utf-8') \
                as twu_file:

            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)
            data_twu = json.load(twu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data_twu, status=200)

            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 3

            issue_id, url, title = open_issues[0]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'  # noqa: E501
            assert title == 'First CWU Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == 'd2a6aca3-7143-41bc-99a7-8ce7014ac3af'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/d2a6aca3-7143-41bc-99a7-8ce7014ac3af'  # noqa: E501
            assert title == 'Second CWU Issue'

            issue_id, url, title = open_issues[2]
            assert issue_id == 'ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'
            assert url == 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'  # noqa: E501
            assert title == 'First TWU Issue'

    @responses.activate
    def test_one_twu_issue(self):
        with open('tests/data/one_issue_twu.json', encoding='utf-8') \
            as twu_file, \
                open('tests/data/no_issues.json', encoding='utf-8') \
                as empty_file:
            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()
            data_empty = json.load(empty_file)
            data_twu = json.load(twu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_empty, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_empty, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data_twu, status=200)
            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 1

            issue_id, url, title = open_issues[0]
            assert issue_id == 'ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'
            assert url == 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/ffe3be71-bd4b-4b90-ab41-ec9147be4a3f'  # noqa: E501
            assert title == 'First TWU Issue'

    @responses.activate
    def test_only_published_opportunities_are_worked_on(self):
        with open('tests/data/three_issues_cwu.json', encoding='utf-8') \
                as cwu_file, \
                open('tests/data/three_issues_swu.json', encoding='utf-8') \
                as swu_file, \
                open('tests/data/three_issues_twu.json', encoding='utf-8') \
                as twu_file:

            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()
            data_swu = json.load(swu_file)
            data_cwu = json.load(cwu_file)
            data_twu = json.load(twu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_swu, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_cwu, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=data_twu, status=200)

            open_issues = models.BCDevExchangeIssues().get_opportunities()
            assert len(open_issues) == 3

            issue_id, url, title = open_issues[0]
            assert issue_id == '04003a5f-f609-469f-91bb-f3c6ac56bed7'
            assert url == \
                'https://digital.gov.bc.ca/marketplace/opportunities/sprint-with-us/04003a5f-f609-469f-91bb-f3c6ac56bed7'  # noqa: E501
            assert title == 'Third Issue'

            issue_id, url, title = open_issues[1]
            assert issue_id == 'f1f6aca3-7143-41bc-99a7-8ce7014ac242'
            assert url == 'https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/f1f6aca3-7143-41bc-99a7-8ce7014ac242'  # noqa: E501
            assert title == 'First CWU Issue'

            issue_id, url, title = open_issues[2]
            assert issue_id == '6732be71-bd4b-451f-ab41-2af35fe4903a'
            assert url == 'https://marketplace.digital.gov.bc.ca/opportunities/team-with-us/6732be71-bd4b-451f-ab41-2af35fe4903a'  # noqa: E501
            assert title == 'Third TWU Issue'

    @responses.activate
    def test_unknown_status_is_handled(self):
        expected_log = 'ERROR:bcdevexbot.models:Unknown status NEW for issue c9995fe1-0826-4f9a-88d9-f109c7f67b3c - New Opportunity'  # noqa: E501
        with open('tests/data/unknown_status.json', encoding='utf-8') \
                as bad_status_file, \
                open('tests/data/no_issues.json', encoding='utf-8') \
                as swu_file, \
                open('tests/data/one_issue_twu.json', encoding='utf-8') \
                as twu_file:

            swu = models.SprintWithUsOpportunity()
            cwu = models.CodeWithUsOpportunity()
            twu = models.TeamWithUsOpportunity()

            data_empty = json.load(swu_file)
            data_bad_status = json.load(bad_status_file)
            twu_data = json.load(twu_file)

            responses.add(responses.GET, swu.api_url,
                          json=data_empty, status=200)
            responses.add(responses.GET, cwu.api_url,
                          json=data_bad_status, status=200)
            responses.add(responses.GET, twu.api_url,
                          json=twu_data, status=200)

            with self.assertLogs('bcdevexbot.models', level='ERROR') as log_context:  # noqa: E501
                open_issues = models.BCDevExchangeIssues().get_opportunities()
                assert len(open_issues) == 1
                assert len(log_context.output) == 1
                self.assertIn(expected_log, log_context.output)


if __name__ == '__main__':
    unittest.main()
