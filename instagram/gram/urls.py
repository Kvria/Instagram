from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'welcome'),
    url('^index/', views.home, name='index'),
    url(r'^profile/', views.profile, name='profile')

]