from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_news, name='news_list'),
]