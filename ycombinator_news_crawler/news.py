from ycombinator_news_crawler.config import BASE_URL
from ycombinator_news_crawler.model import News
from datetime import date
from re import compile
from requests import get
from bs4 import BeautifulSoup


def _get_news(amount: int, news_type: str) -> list[News]:
    result = []
    next_page = news_type
    while len(result) < amount and next_page is not None:
        resp = get(f"{BASE_URL}/{next_page}")
        body = BeautifulSoup(resp.text, "html.parser")

        next_page = body.find(class_="morelink")
        # is None when last page otherwise next page link
        next_page = next_page.attrs["href"] if next_page is not None else None

        news_list = body.find_all(class_="athing")
        for news in news_list:

            if len(result) >= amount:
                return result

            news_title = news.find(class_="titlelink").text
            news_id = news.attrs["id"]
            news_link = news.find(class_="titlelink").attrs["href"]

            # extract sub info
            sub_info = news.next_sibling.find(class_="subtext")
            point = int(sub_info.find(class_="score").text.split()[0])
            age = sub_info.find(class_="age").attrs["title"]
            # use \s here there is \xa0 non-breaking space in between
            comment_info = sub_info.find(string=compile(r"\d+\scomment"))
            if comment_info is not None:
                comment_count = int(comment_info.split()[0])
            else:
                comment_count = 0

            username = sub_info.find(class_="hnuser").text

            result.append(News(news_title, news_id, news_link, point, username, age, comment_count))

    return result


def get_newest(amount: int = 30) -> list[News]:
    return _get_news(amount, "newest")


def get_past(amount: int = 30, search_date: str = None) -> list[News]:
    if search_date is None:
        search_date = date.today().strftime("%Y-%m-%d")

    return _get_news(amount, f"front?day={search_date}")


def get_ask(amount: int = 30) -> list[News]:
    return _get_news(amount, "ask")


def get_show(amount: int = 30) -> list[News]:
    return _get_news(amount, "show")


if __name__ == "__main__":
    ls = get_past(100, "2022-05-07")
    print(f"count: {len(ls)}, title: {str(ls[0])}")
    pass
