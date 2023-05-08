from collections import Counter
from tech_news.database import find_news


def top_5_categories():
    all_categories = [news["category"] for news in find_news()]
    categories_count = Counter(all_categories)
    top_categories = categories_count.most_common(5)
    return [category[0] for category in top_categories]
