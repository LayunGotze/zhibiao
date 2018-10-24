import re
import json
from api.use.mongodb_link import events_tracking
from api.use.geo_lat_lon import geo2lat
name2code_dict={}
with open('code.txt','r') as f:
    name2code_dict=json.loads(f.read())


def event_combine_by_name(actor1name,actor2name):
    #根据ACTOR1和ACTOR2查找时间回溯信息，包括时间和地点,不包括经纬度
    #ret = event_combine_by_name("President", "China")
    if actor1name in name2code_dict and actor2name in name2code_dict:
        res = events_tracking.find({"actor1name": actor1name, "actor2name": actor2name,
                                "actor1code": {"$in": name2code_dict[actor1name]},
                                "actor2code": {"$in": name2code_dict[actor2name]}})
    elif actor1name not in name2code_dict:
        return {"meg":"no name "+actor1name}
    else:
        return {"meg":"no name "+actor2name}
    if(res.count()==0):
        return {"total":0}
    """
    want_key=['sqldate','sentid','actor1geo_long', 'actiongeo_fullname', 'actor1geo_adm1code',
              'actiongeo_lat', 'actor2geo_countrycode', 'actor2geo_type', 'actor1geo_lat',
              'actor1geo_fullname', 'actor2geo_long', 'actor2geo_lat', 'actor1geo_type',
              'actiongeo_adm1code', 'actiongeo_featureid', 'actor1geo_countrycode', 'actiongeo_long',
              'actor1geo_featureid', 'actor2geo_featureid', 'actor2geo_adm1code', 'actiongeo_type',
              'actor2geo_fullname', 'actiongeo_countrycode']
    """
    want_key=['sqldate','sentid','actor2geo_fullname','actor1geo_fullname']
    geo_key=['actor2geo_fullname','actor1geo_fullname']

    ret={}
    ret['total']=res.count()
    list=[]
    for item in res:
        tmp_dict={}
        for key in want_key:
            if key in item:
                tmp_dict[key]=item[key]
            else:
                tmp_dict[key]="null"
        """
        for key in geo_key:
            if tmp_dict[key]!="null":
                tmp_dict['lat'],tmp_dict['log']=geo2lat(tmp_dict[key])
        """
        list.append(tmp_dict)
    ret['res']=list
    ret['actor1name']=actor1name
    ret['actor2name']=actor2name
    return ret

def all_geo2lat(dict):
    #接受event_combine_by_name的全部返回值，将里面的地址名称加入经纬度信息
    #在原基础上将GEOFULLNAME改为 {"name":"asdas","lat":123,"log":123}的形式
    list=dict['res']
    geo_key=['actor2geo_fullname','actor1geo_fullname']
    map={}
    print("!@#!@#")
    for item in list:
        for key in geo_key:
            if item[key]!="null" and key not in map:
                tmp={}
                tmp['name']=item[key]
                tmp['lat'],tmp['log']=geo2lat(item[key])
                item[key]=tmp
                map[key]=tmp
            elif item[key]!="null" and key in map:
                item[key]=map[key]
    return dict

print(all_geo2lat(event_combine_by_name('President','China')))