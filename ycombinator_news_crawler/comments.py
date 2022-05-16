from ycombinator_news_crawler.config import BASE_URL
from ycombinator_news_crawler.model import Comment
from datetime import date
from re import search
from requests import get
from bs4 import BeautifulSoup


def _get_commant(news_id, amount=30):
    URL = rf"https://news.ycombinator.com/item?id={news_id}"

    result = []

    resp = get(URL)
    body = BeautifulSoup(resp.text, "html.parser")

    comments = body.find_all("td", class_="default")
    for comment in comments:

        if len(result) >= amount:
            break

        comment.find(class_="reply").decompose()
        username = comment.find(class_="hnuser").text.strip()
        comment_id = comment.find(class_="age").find("a").attrs["href"]
        comment_id = search(r"item\?id=(.+)", comment_id).group(1).strip()
        age = comment.find(class_="age").attrs["title"].strip()
        content = comment.find(class_="comment").text.strip()
        result.append(Comment(comment_id, username, age, content))

    return result


if __name__ == "__main__":
    ls = _get_commant("31377991")
    print(f"count: {len(ls)}, title: {str(ls[0])}")
    pass
