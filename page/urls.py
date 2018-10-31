from django.contrib import admin
from page.views import *
from django.conf.urls import include, url
urlpatterns=[
    url('map',world_map),
    url('timeline',time_line),
    url('test',test)
]