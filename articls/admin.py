from django.contrib import admin
from .models import Article, ArticleSlider
from django_summernote.admin import SummernoteModelAdmin


class Editcreate(SummernoteModelAdmin):
      summernote_fields = ('body',)

admin.site.register(Article, Editcreate )
admin.site.register(ArticleSlider)
