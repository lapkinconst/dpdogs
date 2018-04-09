# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=256, verbose_name='Название изображения')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание изображения')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('image', models.ImageField(upload_to='images/blog')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'изображения',
            },
        ),
    ]