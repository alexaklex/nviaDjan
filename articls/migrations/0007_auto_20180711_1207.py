# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-11 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articls', '0006_auto_20180706_0827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]