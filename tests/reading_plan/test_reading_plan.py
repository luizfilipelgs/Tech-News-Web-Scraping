from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from tests.reading_plan.mock_news import mocked_news
import pytest
from unittest.mock import MagicMock


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)

    ReadingPlanService._db_news_proxy = MagicMock(return_value=mocked_news)
    res = ReadingPlanService.group_news_for_available_time(12)

    assert len(res['readable']) == 2
    assert len(res['unreadable']) == 1
