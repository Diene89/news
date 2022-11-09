from tech_news.database import search_news


def formatted_news_elements(news):
    news_list = []

    for new in news_list:
        formatted_news = (new["title"], new["url"])
        news_list.append(formatted_news)

    return news_list


def search_by_title(title):
    news_list = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )
  
    return formatted_news_elements(news_list)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
