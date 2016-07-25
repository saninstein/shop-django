from django.contrib import admin
from shop.models import Phone, Category, Slide, Tablet, Notebook, Accessories, ForHome, ForMaster, Order
admin.site.register(Phone)
admin.site.register(Tablet)
admin.site.register(Notebook)
admin.site.register(Category)
admin.site.register(Slide)
admin.site.register(Accessories)
admin.site.register(ForHome)
admin.site.register(ForMaster)
admin.site.register(Order)

# Register your models here.
