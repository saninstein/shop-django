from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^$', views.general, name='general'),
    url(r'^phone/(?P<item>\d+)/$', views.item_phone, name='item_phone'),
    url(r'^phones/$', views.phones, name='phones'),
    url(r'^ajax_search/(?P<search_str>[\w\-]+)/$', views.search),
]