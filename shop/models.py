import PIL
import random
import string
from os import remove
from django.db import models
from elektroswit.settings import ERROR_LOG
from django.db.models import Max

available = (('is', "В наличии"), ('c', "Под заказ"))
cores = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (6, '6'), (8, '8'), (12, '12'))


def compress_img(path, size):
    img = PIL.Image.open(path)
    img.thumbnail(size, PIL.Image.ANTIALIAS)
    bg = PIL.Image.new('RGB', size, (255, 255, 255))
    bg.paste(img, ((size[0] - img.size[0]) // 2, (size[1] - img.size[1]) // 2))
    if size == (250, 250):
        thumb_path = path.split('.')
        thumb_path = thumb_path[0] + '_thumb.' + thumb_path[1]
        bg.save(thumb_path)
    else:
        remove(path)
        bg.save(path)


def get_uniq_name(instance, filename):
    if type(instance) == Slide:
        new_name = 'slides/'
        new_name += ''.join(random.sample(string.ascii_lowercase, 6))
    else:
        new_name = ''.join(random.sample(string.ascii_lowercase, 6))
    new_name += filename[filename.find('.'):]
    return new_name


def upload_path(instance, filename):
    return '{0}/{1}/{2}'.format(instance.link_category.id, instance.name, get_uniq_name(instance, filename))


def get_inv():
    item = Items.objects.get(pk=1)
    a = [item.phone_set, item.tablet_set, item.notebook_set]
    num = []
    for i in a:
        agr = i.aggregate(max=Max('inv'))
        if agr['max'] != None:
            num.append(agr['max'])
    if len(num):
        return max(num) + 1
    else:
        return 1


class Items(models.Model):
    name = models.CharField(max_length=200, default='')


class Category(models.Model):
    name = models.CharField(default='Категория', max_length=100, verbose_name="Название", null=False, blank=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    class Meta:
        abstract = True
        ordering = ["-date"]

    name = models.CharField(max_length=100, verbose_name='Название', help_text='Введите название', default='')
    availability = models.CharField(max_length=100, verbose_name='Наличие', choices=available, default=available[0])
    photo = models.ImageField(verbose_name='Главное фото', upload_to=upload_path, blank=False)
    photo1 = models.ImageField(verbose_name='Фото 1', upload_to=upload_path, blank=True)
    photo2 = models.ImageField(verbose_name='Фото 2', upload_to=upload_path, blank=True)
    photo3 = models.ImageField(verbose_name='Фото 3', upload_to=upload_path, blank=True)
    photo4 = models.ImageField(verbose_name='Фото 4', upload_to=upload_path, blank=True)
    photo5 = models.ImageField(verbose_name='Фото 5', upload_to=upload_path, blank=True)
    video = models.URLField(verbose_name='Видеообзор', blank=True)
    description = models.TextField(verbose_name='Описание', max_length=1500, blank=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.DecimalField(verbose_name='Цена в розницу', max_digits=20, decimal_places=2)
    price_opt = models.DecimalField(verbose_name='Цена оптом', max_digits=20, decimal_places=2, default=0)

    diagonal = models.DecimalField(verbose_name='Диагональ', default=0, max_digits=20, decimal_places=2, blank=True)
    resolution = models.CharField(verbose_name='Разрешение экрана', max_length=50, blank=True)
    display_other = models.CharField(verbose_name='Дисплей дополнительно', max_length=200, blank=True)

    wireless = models.CharField(verbose_name='Беспроводные возможности', max_length=500, blank=True)

    interfaces = models.CharField(verbose_name='Интерфейсы и подключения', max_length=500, blank=True)

    battery = models.IntegerField(verbose_name='Ёмкость батареи', default=0, blank=True)

    camera = models.IntegerField(verbose_name='Размер камеры', default=0, blank=True)
    camera_other = models.CharField(verbose_name='Камера дополнительно', max_length=100, blank=True)

    osystem = models.CharField(verbose_name='Операционная система', max_length=500, blank=True)
    count_core = models.IntegerField(verbose_name='Количесво ядер', choices=cores, default=cores[0])
    core_other = models.CharField(verbose_name='Процессор', max_length=200, blank=True)
    ram = models.IntegerField(verbose_name='Оперативная память', default=0, blank=True)
    memory = models.IntegerField(verbose_name='Внутреняя память', default=0, blank=True)
    memory_other = models.CharField(verbose_name='Память дополнительно', max_length=200, blank=True)

    other = models.CharField(verbose_name='Дополнительно', max_length=200, blank=True)
    link_items = models.ForeignKey(Items, default=1, editable=False)
    inv = models.IntegerField(editable=False, default=get_inv)
    likes = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.name

    def get_thumb(self):
        url = self.photo.url
        url = url.split('.')
        thumb_url = url[0] + '_thumb.' + url[1]
        return thumb_url

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)
        try:
            compress_img(self.photo.path, (250, 250))

            compress_img(self.photo.path, (800, 600))
            photos = [self.photo1, self.photo2,
                      self.photo3, self.photo4,
                      self.photo5]
            for photo in photos:
                if photo != '':
                    compress_img(photo.path, (800, 600))
        except BaseException as e:
            f = open(ERROR_LOG, 'a')
            f.write(e)
            f.close()
        finally:
            pass
        
    def get_item(self):
        return '/item/' + str(self.inv)


class Phone(Item):
    standards = models.CharField(verbose_name='Стандарты и техгологии', max_length=100, blank=True)
    front_camera = models.IntegerField(verbose_name='Размер фронтальной камеры', default=0, blank=True)
    front_camera_other = models.CharField(verbose_name='Камера фронтальная дополнительно', max_length=100, blank=True)
    sim_count = models.IntegerField(verbose_name='Количество сим', default=0, blank=True)
    link_category = models.ForeignKey(Category, default=1, editable=False)


class Tablet(Item):
    standards = models.CharField(verbose_name='Стандарты и техгологии', max_length=100, blank=True)
    front_camera = models.IntegerField(verbose_name='Размер фронтальной камеры', default=0, blank=True)
    front_camera_other = models.CharField(verbose_name='Камера фронтальная дополнительно', max_length=100, blank=True)
    sim_count = models.IntegerField(verbose_name='Количество сим', default=0, blank=True)
    link_category = models.ForeignKey(Category, default=2, editable=False)


class Notebook(Item):
    link_category = models.ForeignKey(Category, default=3, editable=False)


class Slide(models.Model):
    img = models.ImageField(upload_to=get_uniq_name, blank=True)

    def save(self, *args, **kwargs):
        super(Slide, self).save(*args, **kwargs)
        try:
            path = self.img.path
            img = PIL.Image.open(path)
            resized_image = img.resize((900, 400), PIL.Image.BILINEAR)
            resized_image.save(path)
        except BaseException as e:
            print(e)
        finally:
            pass

    def __str__(self):
        return 'Слайд' + str(self.id)

    def delete(self, *args, **kwargs):
        remove(self.img.path)
        super(Slide, self).delete(*args, **kwargs)

