# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # thumb мениатюра пользователя кто добавил статью
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'    
