# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import Page
from articls.models import Article

#
def page_about(request):
    # return HttpResponse(slug)
      page = Page.objects.get(id=1)
      sidebar = Article.objects.all().order_by('date')
      return render(request, 'pages/page_detail.html', {'page_detail':page, 'sidebar':sidebar})

def page_contact(request):
    # return HttpResponse(slug)
      page = Page.objects.get(id=2)
      sidebar = Article.objects.all().order_by('date')
      return render(request, 'pages/page_detail.html', {'page_detail':page, 'sidebar':sidebar})
