from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return [(news["title"], news["url"]) for news in search_news(query)]


# Requisito 8
def search_by_date(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d/%m/%Y")
        query = {"timestamp": formatted_date}
        matching_dates = search_news(query)
        return [(news["title"], news["url"]) for news in matching_dates]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    return [(news['title'], news['url']) for news in search_news(query)]
