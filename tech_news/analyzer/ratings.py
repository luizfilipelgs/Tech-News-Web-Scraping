from collections import Counter
from tech_news.database import search_news


def top_5_categories():
    all_news = search_news({})
    all_categories = [news["category"] for news in all_news]
    counted_categories = Counter(all_categories)
    sorted_categories = sorted(counted_categories.items(), key=lambda x: (
        -x[1], x[0]))
    return [category for category, count in sorted_categories[:5]]
