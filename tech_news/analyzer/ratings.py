from collections import Counter
from tech_news.database import search_news


def top_5_categories():
    all_news = search_news({})
    all_categories = [news["category"] for news in all_news]
    counted_categories = Counter(all_categories)
    most_common_categories = counted_categories.most_common(5)
    sorted_categories = sorted(
        most_common_categories,
        key=lambda category: (-category[1], category[0]),
    )
    return [category[0] for category in sorted_categories]
