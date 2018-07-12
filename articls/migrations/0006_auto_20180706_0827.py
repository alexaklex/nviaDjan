# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-06 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articls', '0005_articleslider_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleslider',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='articleslider',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]