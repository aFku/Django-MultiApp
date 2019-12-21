from .template import News


class Interia(News):
    def __init__(self):
        News.__init__(self, 'https://www.interia.pl/')
        # less soup to searching
        self.soup = self.soup.find("section", id="page")

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
        # (Title, article url, img url)
        content = (container.get("title"), container.get("href"), container.img.get('src'))
        return content

    def __get_small_news_photos(self):
        container = self.soup.find("ul", id="facts_photos")
        container = container.find_all("a")
        # (Title, article url, img url)
        content = []
        for line in container:
            content.append((line.get('title'), line.get('href'), line.img.get('src')))
        return content

    def __get_huge_news(self):
        container = self.soup.find("ul", id="tiles_karuzela")
        container = container.find_all("li")
        # (Title, article url, img url)
        content = []
        ''' there is some issue with getting address of img from carousel so need to use other attributes and 
            in tiles_karuzela section last element with ul tag is set of carousel articles so I ignore it because we get
            this on the beginning'''
        for line in container[0:-1]:
            if len(line.get("class")) > 2:
                line = line.a
                img = line.img.get('data-src')
            else:
                line = line.a
                img = line.img.get('src')
            content.append((line.get('title'), line.get('href'), img))
        return content

    def __get_business_img(self):
        container = self.soup.find("div", id="business_news_one").a
        # (Title, article url, img url)
        content = (container.get("title"), container.get("href"), container.img.get('data-src'))
        return content

    def __get_business_small(self):
        container = self.soup.find("ul", id="business_news")
        container = container.find_all("a")
        # Title : url  pairs
        content = {}
        for line in container:
            content[line.get("title")] = line.get('href')
        return content

    def __get_sport_small_photo(self):
        container = self.soup.find("div", id="sport_news_one")
        container = container.a
        # (Title, article url, img url)
        content = (container.get("title"), container.get('href'), container.img.get('data-src'))
        return content

    def __get_sport_small(self):
        container = self.soup.find("ul", id="sport_news")
        container = container.find_all("li")
        # Title : url  pairs
        content = {}
        for line in container:
            content[line.a.get("title")] = line.a.get('href')
        return content

    def get_huge_sport(self):
        container = self.soup.find("div", {"class": "sport-right"})
        container = container.find_all("div")
        # (Title, article url, img url)
        content = []
        for line in container:
            content.append((line.a.get_text(), line.a.get('href'), line.a.img.get('data-src')))
        return content
    

