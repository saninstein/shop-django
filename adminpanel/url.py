from django.conf.urls import url
from adminpanel import views

urlpatterns = [
    url(r'^$', views.general),
    url(r'^new/(?P<category>[\w\-]+)/$', views.new_item, name='new_item'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]