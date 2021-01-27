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
        assert cwu.is_status_closed("EVAL_QUESTIONS")
        assert cwu.is_status_closed("EVAL_CC")
        assert cwu.is_status_closed("EVAL_SCENARIO")
        self.assertFalse(cwu.is_status_closed("PUBLISHED"))

    def test_open_status(self):
        cwu = models.CodeWithUsOpportunity()
        assert cwu.is_status_open("PUBLISHED")
        self.assertFalse(cwu.is_status_open("EVALUATION"))
        self.assertFalse(cwu.is_status_open("AWARDED"))
        self.assertFalse(cwu.is_status_open("EVAL_QUESTIONS"))
        self.assertFalse(cwu.is_status_open("EVAL_CC"))
        self.assertFalse(cwu.is_status_open("EVAL_SCENARIO"))


if __name__ == '__main__':
    unittest.main()
