import requests


# Requisito 1
def fetch(url: str, wait: int = 3) -> str:
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header, timeout=wait)
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


""" url = 'https://g1.globo.com/economia/'
print(fetch(url))
 """


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
