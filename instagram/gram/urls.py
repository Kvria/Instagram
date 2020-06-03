from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'welcome'),
    url('^index/', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url('^search/', views.search_users, name='search_users'),
    url(r'^new/post$', views.post_new, name='new_post'),

]