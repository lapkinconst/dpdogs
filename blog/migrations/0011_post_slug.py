# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171027_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, verbose_name='URL поста'),
            preserve_default=False,
        ),
    ]
