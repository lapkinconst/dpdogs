# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentuser',
            name='age',
            field=models.IntegerField(max_length=3),
        ),
    ]
