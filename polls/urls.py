from django.conf.urls import url
#ssfrom django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
