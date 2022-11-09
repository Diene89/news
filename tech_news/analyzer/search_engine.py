from tech_news.database import search_news
from datetime import datetime


def formatted_news_elements(news):
    news_list = []

    for new in news_list:
        formatted_news = (new["title"], new["url"])
        news_list.append(formatted_news)

    return news_list


def search_by_title(title):
    news_list = search_news({"title": {"$regex": f"{title}", "$options": "i"}})
  
    return formatted_news_elements(news_list)


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news_list = search_news({"timestamp": {"$regex": date, "$options": "i"}})

    return formatted_news_elements(news_list)


def search_by_tag(tag):
    """Seu código deve vir aqui"""

def search_by_category(category):
    """Seu código deve vir aqui"""