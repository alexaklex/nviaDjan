# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import Article, ArticleSlider
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from page.models import Page


def articl_list(request):
    # Получаем все сохраненные объекты из базы тоесть статьи
    articls = Article.objects.all().order_by('date')
    page = Page.objects.all().order_by('date')
    slider = ArticleSlider.objects.filter(is_active=True)
    # Затем третьим параметром указываем словарь, с ключевым словом которое подключается к
    # текущему шаблону это ART со значением переменной
    return render(request, 'articles/articl_list.html', {'art': articls, 'menu':page, 'slider':slider})

def articl_detail(request, slug):
    # return HttpResponse(slug)
      article = Article.objects.get(slug = slug)
      sidebar = Article.objects.all().order_by('date')
      return render(request, 'articles/article_detail.html', {'artdet':article, 'sidebar':sidebar})

def slider_detail(request, slug):
      article = ArticleSlider.objects.get(slug = slug)
      return render(request, 'articles/article_detail.html', {'artdet':article})

def sidebar_detail(request, slug):
      article = ArticleSlider.objects.get(slug = slug)
      return render(request, 'articles/article_detail.html', {'artdet':article})


@login_required(login_url="/account/login/")
def articl_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
         # save articls to db
           instance = form.save(commit=False)
           instance.author = request.user
           instance.save()
           return redirect('articles:list')

    else:
       form = forms.CreateArticle
    return render(request, 'articles/articl_create.html', {'forms':form})
