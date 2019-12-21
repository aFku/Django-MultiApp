from .template import News


class Interia(News):
    def __init__(self):
        News.__init__(self, 'https://www.interia.pl/')

    def __get_small_news(self):
        container = self.soup.find("ul", id="facts_news_small")
        container = container.find_all("a")
        # Title : url  pairs
        content = {}
        for line in container:
            content[line.get("title")] = line.get('href')
        return content

    def __get_small_news_img(self):
        container = self.soup.find("div", id="facts_news_small_one").a
        img = container.img
        # (Title, article url, img url)
        content = (container.get("title"), container.get("href"), img.get('src'))
        return content

    def __get_small_news_photos(self):
        container = self.soup.find("ul", id="facts_photos")
        container = container.find_all("a")
        # (Title, article url, img url)
        content = []
        for line in container:
            content.append((line.get('title'), line.get('href'), line.img.get('src')))
        return content
