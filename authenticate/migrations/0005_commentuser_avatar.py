# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_auto_20171031_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentuser',
            name='avatar',
            field=models.ImageField(default='images/blog/avatar.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]