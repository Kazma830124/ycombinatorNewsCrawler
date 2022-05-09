from hashlib import new
from .config import BASE_URL
from .model import News
from datetime import date
from re import compile
from requests import get
from bs4 import BeautifulSoup

NEWEST_URL = f"{BASE_URL}/newest"


def get_newest(amount: int = 30) -> list[News]:
    result = []

    resp = get(NEWEST_URL)
    body = BeautifulSoup(resp.text, "html.parser")
    news_list = body.find_all(class_="athing")
    for news in news_list:
        news_title = news.find(class_="titlelink").text
        news_id = news.attrs["id"]
        news_link = news.find(class_="titlelink").attrs["href"]

        sub_info = news.next_sibling.find(class_="subtext")
        point = int(sub_info.find(class_="score").text.split()[0])
        age = sub_info.find(class_="age").attrs["title"]
        comment_info = sub_info.find(class_=compile(r"^item\?id=\d+"))
        commentNum = int(comment_info.split()[
                         0]) if comment_info is not None else 0

        username = sub_info.find(class_="hnuser").text

        result.append(News(news_title, news_id,
                      news_link, point, age, commentNum, username))

    return result


def get_news(amount: int = 30, search_date: str = None) -> list[News]:
    if search_date is None:
        search_date = date.today().strftime("%Y-%m-%d")

    raise NotImplementedError()


def get_ask(amount: int = 30) -> list[News]:
    raise NotImplementedError()


def get_show(amount: int = 30) -> list[News]:
    raise NotImplementedError()
