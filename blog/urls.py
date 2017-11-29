from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/(?P<id>\d+)/$', views.articles_detail, name='article_detail'),
    url(r'^contact/$', views.contact, name='contact'),
]
