# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=10, verbose_name='商品品牌名称')),
                ('brand_index', models.IntegerField(default=1, verbose_name='排列顺序')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_type', models.IntegerField(choices=[(0, '手机通讯'), (1, '平板电脑')])),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=10, verbose_name='商品名')),
                ('goods_info', models.CharField(max_length=255, verbose_name='商品描述')),
                ('goods_pic', models.ImageField(upload_to='uploads/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Brand')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category'),
        ),
    ]