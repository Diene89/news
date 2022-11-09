import requests
import time
import parsel
from tech_news.database import create_news


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


def scrape_noticia(html_content):
    selector = parsel.Selector(text=html_content)
    title = selector.css("h1.entry-title::text").get().strip()
    url = selector.css("link[rel=canonical]::attr(href)").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    comments_count = selector.css("div.comment-respond").getall()
    summary = selector.css(
        "div.entry-content > p:nth-of-type(1) *::text"
    ).getall()
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": len(comments_count),
        "summary": "".join(summary).strip(),
        "tags": tags,
        "category": category,
    }


def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    url_news = []

    while len(url_news) <= amount:
        get_page_content = fetch(url)
        get_url_news = scrape_novidades(get_page_content)

        for new in get_url_news:
            news_content = fetch(new)
            url_news.append(scrape_noticia(news_content))
       
        url = scrape_next_page_link(get_page_content)
    create_news(url_news[:amount])
    return url_news[:amount]
