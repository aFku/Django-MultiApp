from django.shortcuts import render
from .news import *


def post_news(request):
    content_interia = Interia().send_news()
    content_cda = CDA().send_news()
    content_imdb = IMDB().send_news()
    return render(request, 'NewsSite/news_list.html', {'content_interia_small_news': content_interia[0],
                                                       'content_interia_small_news_img': content_interia[1],
                                                       'content_interia_small_news_photos': content_interia[2],
                                                       'content_interia_huge_news': content_interia[3],
                                                       'content_interia_business_img': content_interia[4],
                                                       'content_interia_business_small': content_interia[5],
                                                       'content_interia_sport_small_photo': content_interia[6],
                                                       'content_interia_sport_small': content_interia[7],
                                                       'content_interia_huge_sport': content_interia[8],
                                                       'content_cda': content_cda,
                                                       'content_imdb': content_imdb})
