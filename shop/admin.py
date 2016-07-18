from django.contrib import admin
from shop.models import Phone, Category, Slide, Tablet, Notebook
admin.site.register(Phone)
admin.site.register(Tablet)
admin.site.register(Notebook)
admin.site.register(Category)
admin.site.register(Slide)

# Register your models here.
