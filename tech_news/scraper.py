from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url: str, wait: int = 3) -> str:
    time.sleep(1)
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header, timeout=wait)
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


"""
url = 'https://blog.betrybe.com/'
res_fetch = fetch(url) """


# Requisito 2
def scrape_updates(html_content: str) -> list[str]:
    selector = Selector(html_content)
    listUrl = selector.css('.cs-overlay-link::attr(href)').getall()
    return listUrl


""" res_scrap = scrape_updates(res_fetch)
print(res_scrap) """


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
