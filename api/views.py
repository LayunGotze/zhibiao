from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from api.use.read_zb import event_combine_by_name,all_geo2lat
from api.use.find_actor import *
from api.use.geo_lat_lon import *
from api.use.original_text import *
# Create your views here.
tmp={
  "total": 4,
  "res": [
    {
      "sqldate": "20180502",
      "sentid": "5ae994a9aacf802249155fb3_0",
      "actor2geo_fullname": "China",
      "actor1geo_fullname": "Canberra",
      "actor1geo_fullname1": {
        "origin": {
          "msg": "success",
          "res": {
            "title": "France, Australia call on China to observe rules",
            "url": "http://www.miamiherald.com/news/business/article210267264.html#storylink=rss",
            "sent": "French President Emmanuel Macron and Australian Prime Minister Malcolm Turnbull on Wednesday issued a reminder to China to respect a \"rules-based\" order in the South Pacific amid concerns about Beijing's growing influence in the region."
          }
        },
        "time": "20180502",
        "lat": -35.2975906,
        "lon": 149.1012676,
        "color": "red",
        "name": "President",
        "geo": "Canberra"
      },
      "actor2geo_fullname1": {
        "origin": {
          "msg": "success",
          "res": {
            "title": "France, Australia call on China to observe rules",
            "url": "http://www.miamiherald.com/news/business/article210267264.html#storylink=rss",
            "sent": "French President Emmanuel Macron and Australian Prime Minister Malcolm Turnbull on Wednesday issued a reminder to China to respect a \"rules-based\" order in the South Pacific amid concerns about Beijing's growing influence in the region."
          }
        },
        "time": "20180502",
        "lat": 35.000074,
        "lon": 104.999927,
        "color": "blue",
        "name": "China",
        "geo": "China",
        "hub": "Canberra"
      }
    },
    {
      "sqldate": "20180502",
      "sentid": "5ae994b3aacf802249155fc2_0",
      "actor2geo_fullname": "Beijing",
      "actor1geo_fullname": "Canberra",
      "actor1geo_fullname1": {
        "origin": {
          "msg": "success",
          "res": {
            "title": "France, Australia call on China to observe rules",
            "url": "http://www.miamiherald.com/news/business/article210267264.html#storylink=rss",
            "sent": "French President Emmanuel Macron and Australian Prime Minister Malcolm Turnbull on Wednesday issued a reminder to China to respect a \"rules-based\" order in the South Pacific amid concerns about Beijing's growing influence in the region."
          }
        },
        "time": "20180502",
        "lat": -35.2975906,
        "lon": 149.1012676,
        "color": "red",
        "name": "President",
        "geo": "Canberra"
      },
      "actor2geo_fullname1": {
        "origin": {
          "msg": "success",
          "res": {
            "title": "France, Australia call on China to observe rules",
            "url": "http://www.miamiherald.com/news/business/article210267264.html#storylink=rss",
            "sent": "French President Emmanuel Macron and Australian Prime Minister Malcolm Turnbull on Wednesday issued a reminder to China to respect a \"rules-based\" order in the South Pacific amid concerns about Beijing's growing influence in the region."
          }
        },
        "time": "20180502",
        "lat": 39.9059631,
        "lon": 116.391248,
        "color": "blue",
        "name": "China",
        "geo": "Beijing",
        "hub": "Canberra"
      }
    },
    {
      "sqldate": "20180502",
      "sentid": "5ae994a9aacf802249155fb6_0",
      "actor2geo_fullname": "China",
      "actor1geo_fullname": "Canberra",
      "actor1geo_fullname1": {
        "origin": {
          "msg": "success",
          "res": {
            "title": "France, Australia call on China to observe rules",
            "url": "http://www.miamiherald.com/news/business/article210267264.html#storylink=rss",
            "sent": "French President Emmanuel Macron and Australian Prime Minister Malcolm Turnbull on Wednesday issued a reminder to China to respect a \"rules-based\" order in the South Pacific amid concerns about Beijing's growing influence in the region."
          }
        },
        "time": "20180502",
        "lat": -35.2975906,
        "lon": 149.1012676,
        "color": "red",
        "name": "President",
        "geo": "Canberra"
      },
      "actor2geo_fullname1": {
        "origin": {
          "msg": "success",
          "res": {
            "title": "France, Australia call on China to observe rules",
            "url": "http://www.miamiherald.com/news/business/article210267264.html#storylink=rss",
            "sent": "French President Emmanuel Macron and Australian Prime Minister Malcolm Turnbull on Wednesday issued a reminder to China to respect a \"rules-based\" order in the South Pacific amid concerns about Beijing's growing influence in the region."
          }
        },
        "time": "20180502",
        "lat": 35.000074,
        "lon": 104.999927,
        "color": "blue",
        "name": "China",
        "geo": "China",
        "hub": "Canberra"
      }
    },
    {
      "sqldate": "20180506",
      "sentid": "5af29c05aacf80224916d1a7_1",
      "actor2geo_fullname": "China",
      "actor1geo_fullname": "Harare",
      "actor1geo_fullname1": {
        "origin": {
          "msg": "success",
          "res": {
            "title": "Zimbabwe Election Campaigns Ask: What about China?",
            "url": "https://www.voazimbabwe.com/a/zimbabwe-election-campaigns-ask-what-about-china-/4381584.html",
            "sent": "Zimbabwean President Emmerson Mnangagwa is courting both China and the West, saying that Zimbabwe, after decades of pariah status, is \" open for business. \""
          }
        },
        "time": "20180506",
        "lat": -17.831773,
        "lon": 31.045686,
        "color": "red",
        "name": "President",
        "geo": "Harare"
      },
      "actor2geo_fullname1": {
        "origin": {
          "msg": "success",
          "res": {
            "title": "Zimbabwe Election Campaigns Ask: What about China?",
            "url": "https://www.voazimbabwe.com/a/zimbabwe-election-campaigns-ask-what-about-china-/4381584.html",
            "sent": "Zimbabwean President Emmerson Mnangagwa is courting both China and the West, saying that Zimbabwe, after decades of pariah status, is \" open for business. \""
          }
        },
        "time": "20180506",
        "lat": 35.000074,
        "lon": 104.999927,
        "color": "blue",
        "name": "China",
        "geo": "China",
        "hub": "Harare"
      }
    }
  ],
  "actor1name": "President",
  "actor2name": "China"
}
def event_combine(request):
    actor1=request.GET.get('actor1','President')
    actor2=request.GET.get('actor2','China')
    ret=event_combine_by_name(actor1,actor2)
    return JsonResponse(ret)

def event_combine_geo(request):
    return JsonResponse(tmp)
    actor1=request.GET.get('actor1','President')
    actor2=request.GET.get('actor2','China')
    ret=event_combine_by_name(actor1,actor2)
    ret=all_geo2lat(ret)
    return JsonResponse(ret)

def find_1_events(request):
    actor1name=request.GET.get('actor1name','null')
    actor1code=request.GET.get('actor1code','null')
    ret=find_actor1_events(actor1name,actor1code)
    return JsonResponse(ret)

def find_2_events(request):
    actor2name=request.GET.get('actor2name','null')
    actor2code=request.GET.get('actor2code','null')
    ret=find_actor2_events(actor2name,actor2code)
    return JsonResponse(ret)

def name2geo(request):
    address=request.GET.get('address','beijing')
    lat,lon=geo2lat(address)
    return JsonResponse({'lat':lat,'lon':lon})

def find_origintext(request):
    id=request.GET.get('id','null')
    index=request.GET.get('index',-1)
    if(id=='null' or index==-1):
        return JsonResponse({'msg':'not enough parameters'})
    ret=find_origin(id,index)
    return JsonResponse(ret)

