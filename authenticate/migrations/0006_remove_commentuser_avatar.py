# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0005_commentuser_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentuser',
            name='avatar',
        ),
    ]
