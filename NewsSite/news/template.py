import requests
import bs4


class News:
    def __init__(self, link):
        self.url = link
        self.soup = bs4.BeautifulSoup(self.__do_request().text, 'html.parser')

    def __do_request(self):
        return requests.get(self.url)
