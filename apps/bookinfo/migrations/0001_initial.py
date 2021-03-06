# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-14 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libray',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='书名')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('pub_host', models.CharField(max_length=20, null=True, verbose_name='发布人')),
                ('category', models.SmallIntegerField(choices=[(0, '经济金融'), (1, '教育考试'), (2, '计算机与网络'), (3, '语言学习'), (4, '其他')], default=4, verbose_name='类别')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='发布日期')),
                ('count', models.IntegerField(null=True, verbose_name='数量')),
                ('abradability', models.IntegerField(null=True, verbose_name='新旧程度')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='图片')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
                'db_table': 'tb_librayr',
            },
        ),
    ]
