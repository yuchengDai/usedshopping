# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180510_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='uname',
            field=models.CharField(default='', max_length=50, verbose_name='收货人'),
        ),
    ]
