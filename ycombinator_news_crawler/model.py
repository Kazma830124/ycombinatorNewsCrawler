class News:
    def __init__(self, news_title, news_id, news_link, points, username, post_time, comments_count):
        self.news_title = news_title
        self.news_id = news_id
        self.news_link = news_link
        self.points = points
        self.user = username
        self.post_time = post_time
        self.comments_count = comments_count

    def formatOutput(self):
        # return '{}\nlink: {}\npoints: {}\n{}\ncommentNum: {}\n'.format(self.news_title, self.news_link, self.points, self.post_time, self.comments_count)
        return f"""title:{self.news_title}
link:{self.news_link}
point:{self.points}
user:{self.user}
post time:{self.post_time}
comments count:{self.comments_count}
"""

    def __str__(self):
        return self.formatOutput()
