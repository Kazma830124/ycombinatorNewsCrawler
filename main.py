import bs4 as bs
import requests as req


class Model:
    def __init__(self, title, id, link, points, agoTime, commentsNum):
        self.title = title
        self.id = id
        self.link = link
        self.points = points
        self.agoTime = agoTime
        self.commentsNum = commentsNum

    def formatOutput(self):
        return '{}\nlink: {}\npoints: {}\n{}\ncommentNum: {}\n'.format(self.title, self.link, self.points, self.agoTime, self.commentsNum)


def fetchSubInfo(subInfoList: list) -> tuple[int, int, int]:
    points: int = 0
    agoTime: str = ""
    commentNum: int = 0
    for subInfo in subInfoList:
        if type(subInfo.text) is str:
            if subInfo.text.find("points") != -1:
                points = int(subInfo.text.split()[0])
            elif subInfo.text.find("ago") != -1:
                agoTime = subInfo.text
            elif subInfo.text.find("comment") != -1:
                commentNum = int(subInfo.text.split()[0])
            elif subInfo.text == "discuss" != -1:
                continue
            else:
                raise Exception("Unknown subInfo: " + subInfo.text)
        else:
            raise TypeError("subInfo.text is not a string")
    # print(f"points: {points}, agoTime: {agoTime}, commentNum: {commentNum}")
    return points, agoTime, commentNum


url = "https://news.ycombinator.com"
httpRet = req.get(url)
body = bs.BeautifulSoup(httpRet.text, "html.parser")
titleList = body.findAll(class_="athing")
newsList = list[Model]()


for title in titleList:
    id = title.attrs["id"]
    titlelink = title.find(class_="titlelink").attrs["href"]
    subInfoList = body.findAll(id=f"score_{id}") + body.findAll(href=f'item?id={id}')
    points, agoTime, commentNum = fetchSubInfo(subInfoList)
    newsList.append(Model(title.text, id, titlelink, points, agoTime, commentNum))

with open("news.txt", "w", encoding="utf-8") as outFile:
    for news in newsList:
        outFile.writelines(news.formatOutput() + "\n")
    outFile.close()
    
if __name__ == "__main__":
    for news in newsList:
        print(news.formatOutput())