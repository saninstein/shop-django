# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 13:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='camera_other',
            field=models.CharField(blank=True, max_length=100, verbose_name='Камера дополнительно'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 7, 16, 13, 2, 31, 328374, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='phone',
            name='diagonal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, verbose_name='Диагональ'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена в розницу'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price_opt',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена оптом'),
        ),
    ]