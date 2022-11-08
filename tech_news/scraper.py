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


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
