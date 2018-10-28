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
eventcode_dict={'说': 10, '做': 121, '担忧': 12, '相信': 13,
   '拒绝': 14, '承认': 15, '否认': 16,
   '尊重': 17, '同情': 18, '赞同': 19,
   '寻求': 20, '寻求帮助': [21,22,23,103],
   '寻求认同': 24, '呼吁克制': 25, '寻求对话': 26, '寻找办法': 27,
   '会面调解': [28,106], '计划': 30, '将提供帮助': [31,33], '将会影响': 32,
   '为选举投票': 34, '将允许': 35, '会面': 36, '达成条约': 37,
   '将干预': 38, '面临': 40, '致电': 41, '拜访': [42,43],
   '举办会议': 44, '中介调解': 45, '支持': 50, '称赞': [51,52],
   '希望结束': 53, '建立外交关系': 54, '道歉': 55, '原谅': 56,
   '签署条约': 57, '给予': 60, '支付': 61, '装备': 62, '引渡': 63,
   '寻求信息': 64, '贡献': 70, '获得收入': 71,
   '携带武器': 72, '救援': 73, '保护': 74, '避难': 75, '允许': 80, '证明无罪': 81,
   '辞职': 83, '释放': 84, '制裁': 85, '呼吁停止': 87,
   '呼吁调查': [90,91], '主管': 92,
   '视察军队': 93, '调查屠杀': 94, '寻求解释': 101,
   '揭露': 102, '要求撤回': 105,
   '镇压': 110, '宣誓就职': 111, '职责': 112,
   '反对': 113, '抱怨': 114}
def event_combine(request):
    actor1=request.GET.get('actor1','President')
    actor2=request.GET.get('actor2','China')
    ret=event_combine_by_name(actor1,actor2)
    return JsonResponse(ret)

def event_combine_geo(request):
    #return JsonResponse(tmp)
    actor1=request.GET.get('actor1','President')
    actor2=request.GET.get('actor2','China')
    eventcode=request.GET.get('code',-1)
    eventcode=str(eventcode)
    if eventcode not in eventcode_dict:
        eventcode=-1
    else:
        eventcode=eventcode_dict[eventcode]
    #可能存在eventcode是list的问题！
    start=request.GET.get('start','')
    end=request.GET.get('end','')
    if start!='':
      start=start.replace('-','')
    if end!='':
      end=end.replace('-','')
    print(start)
    print(end)
    ret=event_combine_by_name(actor1,actor2,eventcode,start,end)
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

