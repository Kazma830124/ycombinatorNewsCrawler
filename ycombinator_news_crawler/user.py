from ycombinator_news_crawler.config import BASE_URL
from ycombinator_news_crawler.model import User
from ycombinator_news_crawler.news import _get_news
from datetime import date
from re import compile, search
from requests import get
from bs4 import BeautifulSoup


def get_user(username):
    URL = rf"https://news.ycombinator.com/user?id={username}"
    resp = get(URL)
    body = BeautifulSoup(resp.text, "html.parser")
    created = body.find(href=compile(r"day=(.+)&birth"))
    created = search(r"day=(.+)&birth", created.attrs["href"]).group(1).strip()

    karma = body.find("td", string="karma:")
    karma = karma.next_sibling.text.strip()
    karma = int(karma)

    about = body.find("td", string="about:")
    about = about.next_sibling.text.strip()

    return User(username, created, karma, about)


def get_user_submitted(username, amount=30):
    news = _get_news(amount, f"submitted?id={username}")
    return news


def get_user_favorites(username, amount=30):
    news = _get_news(amount, f"favorites?id={username}")
    return news


if __name__ == "__main__":
    news = get_user_favorites('droopyEyelids')
    print(news[0].formatOutput())
    pass
