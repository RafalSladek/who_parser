import urllib.request


class WHODataAPI:
    def __init__(self):
        self.baseUrl = "http://apps.who.int/gho/athena/api/"
        self.format = "foramt=json"
        self.encoding = "utf8"

    def get_who_dimensions(self):
        return urllib.request.urlopen(self.baseUrl + "?" + self.format).read().decode(self.encoding)


