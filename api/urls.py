from django.contrib import admin
from django.conf.urls import include, url
from api.views import *
urlpatterns=[
    url('event_combine',event_combine),
    url('event_geo',event_combine_geo),
    url('find1_events',find_1_events),
    url('find2_events',find_2_events),
    url('togeo',name2geo),
    url('origin',find_origintext)
]