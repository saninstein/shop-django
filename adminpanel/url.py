from django.conf.urls import url
from adminpanel import views

urlpatterns = [
    url(r'^$', views.general),
    url(r'^new/(?P<category>[\w\-]+)/$', views.new_item, name='new_item'),
]