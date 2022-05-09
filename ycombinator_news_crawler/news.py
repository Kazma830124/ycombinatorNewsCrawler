from .config import BASE_URL
from .model import News
from datetime import date
from requests import get
from bs4 import BeautifulSoup

NEWEST_URL = f"{BASE_URL}/newest"


def get_newest(amount: int = 30) -> list[News]:
    result = []

    resp = get(NEWEST_URL)
    body = BeautifulSoup(resp.text, "html.parser")
    news_list = body.find_all(class_="athing")
    for news in news_list:
        news_id = news.attrs["id"]
        news_link = news.find(class_="titlelink").attrs["href"]

        sub_info = news.next_sibling.find_all(class_="subtext")
        #
    pass


def get_news(amount: int = 30, search_date: str = None) -> list[News]:
    if search_date is None:
        search_date = date.today().strftime("%Y-%m-%d")

    raise NotImplementedError()


def get_ask(amount: int = 30) -> list[News]:
    raise NotImplementedError()


def get_show(amount: int = 30) -> list[News]:
    raise NotImplementedError()
