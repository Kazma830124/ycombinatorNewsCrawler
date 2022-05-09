class News:
    def __init__(self, title, id, link, points, agoTime, commentsNum):
        self.title = title
        self.id = id
        self.link = link
        self.points = points
        self.agoTime = agoTime
        self.commentsNum = commentsNum

    def formatOutput(self):
        return '{}\nlink: {}\npoints: {}\n{}\ncommentNum: {}\n'.format(self.title, self.link, self.points, self.agoTime, self.commentsNum)

    def __str__(self):
        return self.formatOutput()
