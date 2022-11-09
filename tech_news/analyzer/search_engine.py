from datetime import datetime

from tech_news.database import search_news


def formatted_news_elements(news):
    news_list = []

    for new in news:
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
    news_list = search_news({"sources": {"$regex": tag, "$options": "i"}})

    return formatted_news_elements(news_list)


def search_by_category(category):
    news_list = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )

    return formatted_news_elements(news_list)
