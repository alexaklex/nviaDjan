# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-23 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default=b'default.png', upload_to=b''),
        ),
    ]