from django.contrib import admin
from shop.models import Phone, Category, Slide, Tablet, Notebook, Accessories
admin.site.register(Phone)
admin.site.register(Tablet)
admin.site.register(Notebook)
admin.site.register(Category)
admin.site.register(Slide)
admin.site.register(Accessories)

# Register your models here.
