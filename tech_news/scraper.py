from tech_news.database import create_news
from parsel import Selector
import requests
import time
import re


def fetch(url: str, wait: int = 3) -> str:
    time.sleep(1)
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header, timeout=wait)
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


def scrape_updates(html_content: str) -> list[str]:
    selector = Selector(html_content)
    listUrl = selector.css('.cs-overlay-link::attr(href)').getall()
    return listUrl


def scrape_next_page_link(html_content: str) -> str:
    selector = Selector(html_content)
    url_next_pag = selector.css('a.next.page-numbers::attr(href)').get()
    if url_next_pag and re.match('^https?://', url_next_pag):
        return url_next_pag
    return None


def scrape_news(html_content: str) -> dict:
    new = {}
    selector = Selector(html_content)
    new['url'] = selector.css("link[rel='canonical']::attr(href)").get()
    new['title'] = selector.css('h1.entry-title::text').get().strip()
    new['timestamp'] = selector.css('li.meta-date::text').get().strip()
    new['writer'] = selector.css('a.url.fn.n::text').get()
    new['reading_time'] = int(selector.css('li.meta-reading-time::text').
                              re_first(r'\d+'))
    new['summary'] = "".join(
        selector.css(".entry-content > p:nth-of-type(1) *::text").
        getall()).strip()
    new['category'] = selector.css('span.label::text').get()
    return new


def get_tech_news(amount):
    html_page = fetch("https://blog.betrybe.com/")
    urls = scrape_updates(html_page)
    news_list = []

    while len(urls) < amount:
        next_page = scrape_next_page_link(html_page)
        html_page = fetch(next_page)
        news_urls = scrape_updates(html_page)
        for new_url in news_urls:
            urls.append(new_url)

    for url in urls[:amount]:
        news_list.append(scrape_news(fetch(url)))

    create_news(news_list)

    return news_list
