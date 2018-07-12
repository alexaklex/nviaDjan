# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

# пока я не понял что это за переменная, но она позволяет добавлять слово articles к name и все магическим образом работает
app_name = 'articles'

urlpatterns = [
    url(r'^$', views.articl_list, name='list'),
    url(r'^create/$', views.articl_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.articl_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.slider_detail, name='slider_detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.sidebar_detail, name='sidebar_detail'),

]
