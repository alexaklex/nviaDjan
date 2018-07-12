# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import Page
from django.http import HttpResponse
from django.conf.urls import url
from .import views
from articls import views as views_art_fr_detail


# пока я не понял что это за переменная,
# но она позволяет добавлять слово articles к name и все магическим образом работает
app_name = 'pages'

urlpatterns = [
    # url(r'^$', views.articl_list, name='list'),
    url(r'^about/$', views.page_about, name='detail_about'),
    url(r'^contact/$', views.page_contact, name='detail_contact'),
    url(r'^contact/$', views.page_contact, name='detail_contact'),
    url(r'^(?P<slug>[\w-]+)/$', views_art_fr_detail.sidebar_detail, name='sidebar_detail'),
]
