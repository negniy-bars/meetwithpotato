# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-14 12:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('potato', '0003_auto_20190414_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likedone',
        ),
        migrations.AddField(
            model_name='post',
            name='likedone',
            field=models.ManyToManyField(related_name='likeforpost', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnumber',
            field=models.IntegerField(default=0, help_text='Начинается с 0', verbose_name='Число лайков'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
