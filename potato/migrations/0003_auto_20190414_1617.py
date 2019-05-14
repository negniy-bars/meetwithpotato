# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-14 11:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('potato', '0002_auto_20190413_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnumber', models.IntegerField(default=0, help_text='Начинается с 0', verbose_name='Число лайков')),
                ('likedone', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likedone',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='thumbnumber',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likedone',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnumber',
        ),
    ]
