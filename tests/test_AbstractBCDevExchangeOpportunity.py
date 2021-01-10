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

    def test_closed_statuses(self):
        cwu = models.CodeWithUsOpportunity()
        assert cwu.is_status_closed("AWARDED")
        assert cwu.is_status_closed("EVALUATION")
        self.assertFalse(cwu.is_status_closed("PUBLISHED"))

    def test_open_status(self):
        cwu = models.CodeWithUsOpportunity()
        assert cwu.is_status_open("PUBLISHED")
        self.assertFalse(cwu.is_status_open("EVALUATION"))
        self.assertFalse(cwu.is_status_open("AWARDED"))


if __name__ == '__main__':
    unittest.main()
