import unittest
import pytest
import responses

from bcdevexbot import models


class SWUTests(unittest.TestCase):

    @responses.activate
    def test_connection_issue_swu(self):
        swu = models.SprintWithUsOpportunity()
        responses.add(responses.GET, swu.api_url,
                      json={"error": "not found"}, status=404)

        with pytest.raises(ConnectionError):
            swu.get_opportunities()


if __name__ == '__main__':
    unittest.main()
