from. template import News


class IMDB(News):
    def __init__(self):
        News.__init__(self, 'https://www.imdb.com/news/movie')
        # less soup
        self.soup = self.soup.find('section', id='news-article-list')

    def __get_news(self):
        url = 'https://www.imdb.com'
        container = self.soup.find_all('article')
        # Title : url  pairs
        content = {}
        for article in container:
            content[article.header.h2.a.get_text()] = url + article.footer.a.get('href')
        return

    def send_news(self):
        return self.__get_news()
