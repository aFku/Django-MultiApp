from .template import News


class CDA(News):
    def __init__(self):
        News.__init__(self, "https://www.cdaction.pl/")
        # less soup to searching
        self.soup = self.soup.find("div", id="content")

    def __get_news(self):
        url = 'https://www.cdaction.pl'
        container = self.soup.find("div", id="newsy")
        container = container.find_all("div", {"class": "news"})
        # (Title, url, img)
        content = []
        for div in container:
            div = div.find("td").a
            content.append((div.img.get('title'), url + div.get('href'), url + div.img.get('src')))
        return content

    def send_news(self):
        return self.__get_news()
