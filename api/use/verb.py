import json
import re
from api.use.mongodb_link import events_tracking
from api.use.geo_lat_lon import geo2lat
from api.use.original_text import *

def fun():
    result={}
    for cnt in range(501,700):
        print(cnt)
        search={'eventcode':cnt}
        res=events_tracking.find(search).limit(100)
        if res.count()==0:
            continue
        dict={}
        for item in res:
            if item['eventverb']!='' and item['eventverb'] not in dict:
                dict[item['eventverb']]=1
            elif item['eventverb']!='':
                dict[item['eventverb']]=dict[item['eventverb']]+1
        tmp=-1
        reskey=''
        for key in dict.keys():
            if dict[key]>tmp:
                tmp=dict[key]
                reskey=key
        if reskey!='' and reskey in dict:
            result[cnt]=reskey
            print(cnt,reskey)
    print("!!!!",result)

def find(id):
    res = events_tracking.find({'eventcode':id})
    if res.count() == 0:
        print("no result")
        return
    dict = {}
    for item in res:
        if item['eventverb'] != '' and item['eventverb'] not in dict:
            dict[item['eventverb']] = 1
        elif item['eventverb'] != '':
            dict[item['eventverb']] = dict[item['eventverb']] + 1
    print(dict)

find(113)