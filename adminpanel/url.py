from django.conf.urls import url
from adminpanel import views

urlpatterns = [
    url(r'^$', views.general, name='admingeneral'),
    url(r'^new/(?P<category>[\w\-]+)/item=(?P<inv>\d+)/$', views.new_item, name='new_item'),
    url(r'^new/(?P<category>[\w\-]+)/$', views.new_item, name='add_item'),
    url(r'^edit/(?P<inv>\d+)/$', views.new_item, name='edit_item'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'edit_slide/(?P<num>\d+)/$', views.slide_edit, name='slide_edit'),
    url(r'^show/(?P<category>[\w\-]+)/$', views.show_items, name='show'),
    url(r'^ajax_delete/$', views.delete_item),
    url(r'^add_share/$', views.add_share, name='add_share'),
]