import requests
import time
import parsel


def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    url_news = selector.css(".cs-overlay-link::attr(href)").getall()
    return url_news


def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page = selector.css(".next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
