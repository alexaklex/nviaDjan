from django.contrib import admin
from .models import Page
from django_summernote.admin import SummernoteModelAdmin


class Editcreate(SummernoteModelAdmin):
      summernote_fields = ('body',)

admin.site.register(Page, Editcreate )
