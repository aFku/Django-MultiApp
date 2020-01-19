from django.urls import path
from . import views

"""Clear path - show main page with all or a part of all questions, this do not send additional data to view
    detail - show all detail about question with id from url. Syntax <int:question_id> will be waiting for integer in
    url and send it to view to argument question_id. This argument must be created with view.
    results and vote are the same as detail but have other tasks."""


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
