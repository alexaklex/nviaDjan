# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # thumb мениатюра пользователя кто добавил статью
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'    



class ArticleSlider(models.Model):
     article = models.ForeignKey(Article, blank=True, null=True, default=None)
     slug = models.SlugField(blank=True, null=True, default=None)
     is_active = models.BooleanField(default=True)
     thumb = models.ImageField(default='default.png', blank=True)

     def __str__(self):
         return self.article.title

     class Meta:
         verbose_name = 'Слайдер'
         verbose_name_plural = 'Слайдеры'
