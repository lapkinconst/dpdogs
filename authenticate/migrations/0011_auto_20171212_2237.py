# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0010_auto_20171212_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentuser',
            name='avatar',
            field=models.ImageField(blank=True, default='../blog/static/media/avatar.jpg', upload_to=''),
        ),
    ]
