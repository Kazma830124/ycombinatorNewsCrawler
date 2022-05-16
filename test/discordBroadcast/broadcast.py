import requests as req
import ycombinator_news_crawler.news as news
newslist = news.get_newest(5)
hookurl = "https://discord.com/api/webhooks/836518466516418610/u5uuQXxQa74VVU2lYQqYu4U6hPQ3QRVytiQO2edrG8Stde7Y5Zeey48D2w6bJAQUAcnl"


formatOutput = ""
for element in newslist:
    formatOutput += element.formatOutput()+"\n"
print(formatOutput)
res = req.post(hookurl, json={"content": formatOutput})
