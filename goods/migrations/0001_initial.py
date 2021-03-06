# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 03:50
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
                ('goods_type', models.CharField(max_length=20, null=True, verbose_name='商品型号')),
                ('brand_grade', models.IntegerField(choices=[(0, 's级'), (1, 'A级'), (2, 'B级'), (3, 'C级')], null=True, verbose_name='商品等级')),
                ('brand_size', models.IntegerField(choices=[(0, '8G'), (1, '16G'), (2, '32G'), (3, '64G'), (5, '128G'), (6, '256G'), (7, '512G')], null=True, verbose_name='容量')),
                ('brand_net', models.IntegerField(choices=[(0, '全网通'), (1, '联通版'), (2, '双4G'), (3, '移动版')], null=True, verbose_name='商品网络')),
                ('brand_color', models.CharField(max_length=10, null=True, verbose_name='商品颜色')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_type', models.IntegerField(choices=[(0, '手机通讯'), (1, '平板电脑')], verbose_name='商品分类')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=10, verbose_name='商品名')),
                ('goods_price', models.FloatField(default=0.0, verbose_name='商品价格')),
                ('goods_num', models.PositiveIntegerField(default=0, verbose_name='商品数量')),
                ('goods_info', models.CharField(max_length=255, verbose_name='商品描述')),
                ('goods_pic', models.ImageField(upload_to='uploads/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Brand', verbose_name='商品对应的品牌规格')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category', verbose_name='商品对应的分类')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category', verbose_name='对应的商品分类'),
        ),
    ]
