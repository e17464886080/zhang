# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-08 09:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='订单号')),
                ('car', models.CharField(max_length=200, verbose_name='车辆信息')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('date', models.DateTimeField(verbose_name='时间')),
                ('orderStatus', models.IntegerField(choices=[(0, '已完成'), (1, '已支付'), (2, '交易关闭'), (3, '订单关闭'), (4, '交易中')], default=0, verbose_name='订单状态')),
                ('idDel', models.BooleanField(default=False, verbose_name='是否删除')),
                ('buy_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buser', to=settings.AUTH_USER_MODEL)),
                ('sale_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '订单信息',
                'db_table': 'Order',
                'verbose_name': '订单信息',
            },
        ),
    ]
