from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock
from tests.reading_plan.mock_news import mock_data


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_data)
    response = ReadingPlanService.group_news_for_available_time(12)

    assert len(response['readable']) == 2
    assert len(response['unreadable']) == 1
    assert response['readable'][0]['unfilled_time'] == 7

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)
