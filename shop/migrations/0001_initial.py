# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Введите название', max_length=100, verbose_name='Название')),
                ('availability', models.CharField(choices=[('is', 'В наличии'), ('c', 'Под заказ')], default=('is', 'В наличии'), max_length=100, verbose_name='Наличие')),
                ('photo', models.ImageField(help_text='Обязательное поле', upload_to=shop.models.upload_path, verbose_name='Главное фото')),
                ('photo1', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 1')),
                ('photo2', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 2')),
                ('photo3', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 3')),
                ('photo4', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 4')),
                ('photo5', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 5')),
                ('video', models.URLField(blank=True, help_text='Введите адрес YouTube видео', verbose_name='Видеообзор')),
                ('description', models.TextField(blank=True, max_length=1500, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Обязательное поле', max_digits=20, verbose_name='Цена в розницу')),
                ('price_opt', models.DecimalField(decimal_places=2, default=0, help_text='Если не надо - оставить нулём', max_digits=20, verbose_name='Цена оптом')),
                ('inv', models.IntegerField(default=shop.models.get_inv, editable=False)),
                ('likes', models.IntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Категория', max_length=100, verbose_name='Название')),
                ('variant', models.IntegerField(choices=[(0, 'Гаджеты'), (1, 'Акссесуары'), (2, 'Для Мастера'), (3, 'Для Дома')], default=(0, 'Гаджеты'))),
            ],
        ),
        migrations.CreateModel(
            name='ForHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Введите название', max_length=100, verbose_name='Название')),
                ('availability', models.CharField(choices=[('is', 'В наличии'), ('c', 'Под заказ')], default=('is', 'В наличии'), max_length=100, verbose_name='Наличие')),
                ('photo', models.ImageField(help_text='Обязательное поле', upload_to=shop.models.upload_path, verbose_name='Главное фото')),
                ('photo1', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 1')),
                ('photo2', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 2')),
                ('photo3', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 3')),
                ('photo4', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 4')),
                ('photo5', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 5')),
                ('video', models.URLField(blank=True, help_text='Введите адрес YouTube видео', verbose_name='Видеообзор')),
                ('description', models.TextField(blank=True, max_length=1500, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Обязательное поле', max_digits=20, verbose_name='Цена в розницу')),
                ('price_opt', models.DecimalField(decimal_places=2, default=0, help_text='Если не надо - оставить нулём', max_digits=20, verbose_name='Цена оптом')),
                ('inv', models.IntegerField(default=shop.models.get_inv, editable=False)),
                ('likes', models.IntegerField(default=0, editable=False)),
                ('link_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Введите название', max_length=100, verbose_name='Название')),
                ('availability', models.CharField(choices=[('is', 'В наличии'), ('c', 'Под заказ')], default=('is', 'В наличии'), max_length=100, verbose_name='Наличие')),
                ('photo', models.ImageField(help_text='Обязательное поле', upload_to=shop.models.upload_path, verbose_name='Главное фото')),
                ('photo1', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 1')),
                ('photo2', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 2')),
                ('photo3', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 3')),
                ('photo4', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 4')),
                ('photo5', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 5')),
                ('video', models.URLField(blank=True, help_text='Введите адрес YouTube видео', verbose_name='Видеообзор')),
                ('description', models.TextField(blank=True, max_length=1500, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Обязательное поле', max_digits=20, verbose_name='Цена в розницу')),
                ('price_opt', models.DecimalField(decimal_places=2, default=0, help_text='Если не надо - оставить нулём', max_digits=20, verbose_name='Цена оптом')),
                ('inv', models.IntegerField(default=shop.models.get_inv, editable=False)),
                ('likes', models.IntegerField(default=0, editable=False)),
                ('link_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Введите название', max_length=100, verbose_name='Название')),
                ('availability', models.CharField(choices=[('is', 'В наличии'), ('c', 'Под заказ')], default=('is', 'В наличии'), max_length=100, verbose_name='Наличие')),
                ('photo', models.ImageField(help_text='Обязательное поле', upload_to=shop.models.upload_path, verbose_name='Главное фото')),
                ('photo1', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 1')),
                ('photo2', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 2')),
                ('photo3', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 3')),
                ('photo4', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 4')),
                ('photo5', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 5')),
                ('video', models.URLField(blank=True, help_text='Введите адрес YouTube видео', verbose_name='Видеообзор')),
                ('description', models.TextField(blank=True, max_length=1500, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Обязательное поле', max_digits=20, verbose_name='Цена в розницу')),
                ('price_opt', models.DecimalField(decimal_places=2, default=0, help_text='Если не надо - оставить нулём', max_digits=20, verbose_name='Цена оптом')),
                ('diagonal', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Диагональ в дюймах', max_digits=20, verbose_name='Диагональ')),
                ('resolution', models.CharField(blank=True, help_text="Вводить через англискую букву 'x'", max_length=50, verbose_name='Разрешение экрана')),
                ('display_other', models.CharField(blank=True, max_length=200, verbose_name='Дисплей дополнительно')),
                ('wireless', models.CharField(blank=True, max_length=500, verbose_name='Беспроводные возможности')),
                ('interfaces', models.CharField(blank=True, max_length=500, verbose_name='Интерфейсы и подключения')),
                ('battery', models.IntegerField(blank=True, default=0, help_text='Ёмкость батареи в mah', verbose_name='Ёмкость батареи')),
                ('camera', models.IntegerField(blank=True, default=0, help_text='Размер камеры в МП', verbose_name='Размер камеры')),
                ('camera_other', models.CharField(blank=True, max_length=100, verbose_name='Камера дополнительно')),
                ('osystem', models.CharField(blank=True, max_length=500, verbose_name='Операционная система')),
                ('count_core', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (6, '6'), (8, '8'), (12, '12')], default=(1, '1'), verbose_name='Количесво ядер')),
                ('core_other', models.CharField(blank=True, max_length=200, verbose_name='Процессор')),
                ('ram', models.IntegerField(blank=True, default=0, help_text='Размер в МБ', verbose_name='Оперативная память')),
                ('memory', models.IntegerField(blank=True, default=0, help_text='Размер в ГБ', verbose_name='Внутреняя память')),
                ('memory_other', models.CharField(blank=True, max_length=200, verbose_name='Память дополнительно')),
                ('other', models.CharField(blank=True, max_length=200, verbose_name='Дополнительно')),
                ('inv', models.IntegerField(default=shop.models.get_inv, editable=False)),
                ('likes', models.IntegerField(default=0, editable=False)),
                ('gpu', models.CharField(blank=True, default='', max_length=300, verbose_name='Видеокарта')),
                ('optical_privod', models.CharField(blank=True, default='', max_length=300, verbose_name='Оптический привод')),
                ('link_category', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('link_items', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='shop.Items')),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Обязательное поле', max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Номер телефона')),
                ('items', models.BinaryField(default=b'none')),
                ('message', models.TextField(blank=True, verbose_name='Сообщение')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Введите название', max_length=100, verbose_name='Название')),
                ('availability', models.CharField(choices=[('is', 'В наличии'), ('c', 'Под заказ')], default=('is', 'В наличии'), max_length=100, verbose_name='Наличие')),
                ('photo', models.ImageField(help_text='Обязательное поле', upload_to=shop.models.upload_path, verbose_name='Главное фото')),
                ('photo1', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 1')),
                ('photo2', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 2')),
                ('photo3', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 3')),
                ('photo4', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 4')),
                ('photo5', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 5')),
                ('video', models.URLField(blank=True, help_text='Введите адрес YouTube видео', verbose_name='Видеообзор')),
                ('description', models.TextField(blank=True, max_length=1500, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Обязательное поле', max_digits=20, verbose_name='Цена в розницу')),
                ('price_opt', models.DecimalField(decimal_places=2, default=0, help_text='Если не надо - оставить нулём', max_digits=20, verbose_name='Цена оптом')),
                ('diagonal', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Диагональ в дюймах', max_digits=20, verbose_name='Диагональ')),
                ('resolution', models.CharField(blank=True, help_text="Вводить через англискую букву 'x'", max_length=50, verbose_name='Разрешение экрана')),
                ('display_other', models.CharField(blank=True, max_length=200, verbose_name='Дисплей дополнительно')),
                ('wireless', models.CharField(blank=True, max_length=500, verbose_name='Беспроводные возможности')),
                ('interfaces', models.CharField(blank=True, max_length=500, verbose_name='Интерфейсы и подключения')),
                ('battery', models.IntegerField(blank=True, default=0, help_text='Ёмкость батареи в mah', verbose_name='Ёмкость батареи')),
                ('camera', models.IntegerField(blank=True, default=0, help_text='Размер камеры в МП', verbose_name='Размер камеры')),
                ('camera_other', models.CharField(blank=True, max_length=100, verbose_name='Камера дополнительно')),
                ('osystem', models.CharField(blank=True, max_length=500, verbose_name='Операционная система')),
                ('count_core', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (6, '6'), (8, '8'), (12, '12')], default=(1, '1'), verbose_name='Количесво ядер')),
                ('core_other', models.CharField(blank=True, max_length=200, verbose_name='Процессор')),
                ('ram', models.IntegerField(blank=True, default=0, help_text='Размер в МБ', verbose_name='Оперативная память')),
                ('memory', models.IntegerField(blank=True, default=0, help_text='Размер в ГБ', verbose_name='Внутреняя память')),
                ('memory_other', models.CharField(blank=True, max_length=200, verbose_name='Память дополнительно')),
                ('other', models.CharField(blank=True, max_length=200, verbose_name='Дополнительно')),
                ('inv', models.IntegerField(default=shop.models.get_inv, editable=False)),
                ('likes', models.IntegerField(default=0, editable=False)),
                ('standards', models.CharField(blank=True, max_length=500, verbose_name='Стандарты и технологии')),
                ('front_camera', models.IntegerField(blank=True, default=0, help_text='Размер камеры в МП', verbose_name='Размер фронтальной камеры')),
                ('front_camera_other', models.CharField(blank=True, max_length=100, verbose_name='Камера фронтальная дополнительно')),
                ('sim_count', models.IntegerField(blank=True, default=1, verbose_name='Количество сим')),
                ('link_category', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('link_items', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='shop.Items')),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('name', models.CharField(default='', editable=False, max_length=600)),
                ('price', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=20)),
                ('inv', models.IntegerField(default=shop.models.get_inv, editable=False, primary_key=True, serialize=False, unique=True)),
                ('gen_item', models.IntegerField()),
                ('sec_item', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to=shop.models.get_uniq_name, verbose_name='Изображение слайда')),
                ('link', models.URLField(blank=True, default='', help_text='Если ссылка не нужна оставить пустым', verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Введите название', max_length=100, verbose_name='Название')),
                ('availability', models.CharField(choices=[('is', 'В наличии'), ('c', 'Под заказ')], default=('is', 'В наличии'), max_length=100, verbose_name='Наличие')),
                ('photo', models.ImageField(help_text='Обязательное поле', upload_to=shop.models.upload_path, verbose_name='Главное фото')),
                ('photo1', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 1')),
                ('photo2', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 2')),
                ('photo3', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 3')),
                ('photo4', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 4')),
                ('photo5', models.ImageField(blank=True, upload_to=shop.models.upload_path, verbose_name='Фото 5')),
                ('video', models.URLField(blank=True, help_text='Введите адрес YouTube видео', verbose_name='Видеообзор')),
                ('description', models.TextField(blank=True, max_length=1500, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Обязательное поле', max_digits=20, verbose_name='Цена в розницу')),
                ('price_opt', models.DecimalField(decimal_places=2, default=0, help_text='Если не надо - оставить нулём', max_digits=20, verbose_name='Цена оптом')),
                ('diagonal', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Диагональ в дюймах', max_digits=20, verbose_name='Диагональ')),
                ('resolution', models.CharField(blank=True, help_text="Вводить через англискую букву 'x'", max_length=50, verbose_name='Разрешение экрана')),
                ('display_other', models.CharField(blank=True, max_length=200, verbose_name='Дисплей дополнительно')),
                ('wireless', models.CharField(blank=True, max_length=500, verbose_name='Беспроводные возможности')),
                ('interfaces', models.CharField(blank=True, max_length=500, verbose_name='Интерфейсы и подключения')),
                ('battery', models.IntegerField(blank=True, default=0, help_text='Ёмкость батареи в mah', verbose_name='Ёмкость батареи')),
                ('camera', models.IntegerField(blank=True, default=0, help_text='Размер камеры в МП', verbose_name='Размер камеры')),
                ('camera_other', models.CharField(blank=True, max_length=100, verbose_name='Камера дополнительно')),
                ('osystem', models.CharField(blank=True, max_length=500, verbose_name='Операционная система')),
                ('count_core', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (6, '6'), (8, '8'), (12, '12')], default=(1, '1'), verbose_name='Количесво ядер')),
                ('core_other', models.CharField(blank=True, max_length=200, verbose_name='Процессор')),
                ('ram', models.IntegerField(blank=True, default=0, help_text='Размер в МБ', verbose_name='Оперативная память')),
                ('memory', models.IntegerField(blank=True, default=0, help_text='Размер в ГБ', verbose_name='Внутреняя память')),
                ('memory_other', models.CharField(blank=True, max_length=200, verbose_name='Память дополнительно')),
                ('other', models.CharField(blank=True, max_length=200, verbose_name='Дополнительно')),
                ('inv', models.IntegerField(default=shop.models.get_inv, editable=False)),
                ('likes', models.IntegerField(default=0, editable=False)),
                ('standards', models.CharField(blank=True, max_length=100, verbose_name='Стандарты и техгологии')),
                ('front_camera', models.IntegerField(blank=True, default=0, verbose_name='Размер фронтальной камеры')),
                ('front_camera_other', models.CharField(blank=True, max_length=100, verbose_name='Камера фронтальная дополнительно')),
                ('sim_count', models.IntegerField(blank=True, default=0, verbose_name='Количество сим')),
                ('link_category', models.ForeignKey(default=2, editable=False, on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('link_items', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='shop.Items')),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='accessories',
            name='link_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Категория'),
        ),
    ]
