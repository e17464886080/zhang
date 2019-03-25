# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-08 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20190308_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='isBan',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (0, '女')], default=1, max_length=10, verbose_name='性别'),
        ),
    ]
