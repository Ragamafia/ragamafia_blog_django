from . import views
# from django.conf.urls import url  # for python 3.8
from django.urls import re_path as url


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),

    url(r'^genres/$', views.GenreListView.as_view(), name='genres'),
    url(r'^genre/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre-detail'),
]