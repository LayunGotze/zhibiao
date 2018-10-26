import re
import json
from api.use.mongodb_link import events_tracking
from api.use.geo_lat_lon import geo2lat
from api.use.original_text import *
name2code_dict={}
with open('code.txt','r') as f:
    name2code_dict=json.loads(f.read())


def event_combine_by_name(actor1name='',actor2name='',eventcode=-1,begindate='',enddate=''):
    #根据ACTOR1和ACTOR2查找时间回溯信息，包括时间和地点,不包括经纬度，完全版
    #必须提供前3个参数，否则要返回错误信息，后面两个时间参数可不写
    #event_combine_by_name('President','China',55,'20180501','20180506')
    #删除没有完全地理信息名称的项
    if eventcode==-1:
        return {"msg":"没有提供事件名称"}
    if actor1name=='' or actor2name=='':
        return {"msg":"需提供参与事件人的姓名"}
    bool_actor1=0
    bool_actor2=0#表示ACTOR1 2 NAME是否在字典中的布尔变量
    if actor1name in name2code_dict:
        bool_actor1=1
    if actor2name in name2code_dict:
        bool_actor2=1
    if bool_actor1==0 and bool_actor2==0:
        #两个姓名都未出现过
        return {'msg':'无搜索结果'}
    eventcode=10
    eventverb='said'
    actor1code=[]
    actor2code=[]
    search_dict = {}
    if begindate!='' and enddate!='':
        search_dict['sqldate']={'$gte':begindate,'$lte':enddate}
    elif begindate!='' and enddate=='':
        search_dict['sqldate'] = {'$gte': begindate}
    elif begindate=='' and enddate!='':
        search_dict['sqldate'] = {'$lte': enddate}
    #排除缺少地理信息的
    search_dict['actor1geo_fullname'] = {"$not": {"$in": ['']}}
    search_dict['actor2geo_fullname'] = {"$not": {"$in": ['']}}
    if bool_actor1==1 and bool_actor2==1:
        #两个姓名都出现了
        actor1code = name2code_dict[actor1name]
        actor2code = name2code_dict[actor2name]
        #search_dict['actor1code']={"$in":actor1code}
        #search_dict['actor2code']={"$in":actor2code}
        search_dict['eventcode']=eventcode
        search_dict['actor1name']=actor1name
        search_dict['actor2name']=actor2name
    if bool_actor1==1 and bool_actor2==0:
        #出现了1没有2
        actor1code = name2code_dict[actor1name]
        search_dict['actor2code'] = {"$in": actor1code}
        search_dict['eventcode'] = eventcode
        search_dict['actor1name'] = actor1name
    if bool_actor1==0 and bool_actor2==1:
        #出现了2没有1
        actor2code = name2code_dict[actor2name]
        search_dict['actor1code'] = {"$in": actor2code}
        search_dict['eventcode'] = eventcode
        search_dict['actor2name'] = actor2name
    #以上都是生成查询语句
    print(search_dict)
    res=events_tracking.find(search_dict)
    if(res.count()==0):
        return {"total":0,"msg":'无结果'}
    """
    want_key=['sqldate','sentid','actor1geo_long', 'actiongeo_fullname', 'actor1geo_adm1code',
              'actiongeo_lat', 'actor2geo_countrycode', 'actor2geo_type', 'actor1geo_lat',
              'actor1geo_fullname', 'actor2geo_long', 'actor2geo_lat', 'actor1geo_type',
              'actiongeo_adm1code', 'actiongeo_featureid', 'actor1geo_countrycode', 'actiongeo_long',
              'actor1geo_featureid', 'actor2geo_featureid', 'actor2geo_adm1code', 'actiongeo_type',
              'actor2geo_fullname', 'actiongeo_countrycode']
    """
    want_key=['sqldate','sentid','actor2geo_fullname','actor1geo_fullname','eventcode','eventverb']

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
    ret['msg']='success'
    ret['actor1name']=actor1name
    ret['actor2name']=actor2name
    return ret

def all_geo2lat(dict):
    #接受event_combine_by_name的全部返回值，将里面的地址名称加入经纬度信息
    #在原基础上将GEOFULLNAME改为 {"name":"asdas","lat":123,"log":123}的形式
    if 'res' not in dict:
        return {'msg':'no result'}
    list=dict['res']
    print(list)
    actor1name=dict['actor1name']
    actor2name=dict['actor2name']
    geo_key=['actor1geo_fullname','actor2geo_fullname']
    map={}
    for item in list:
        for key in geo_key:
            tmp = {}
            tmp['origin'] = find_origin(item['sentid'])
            tmp['time'] = item['sqldate']
            geo=item[key]
            if geo!="null":
                if geo not in map:
                    tmp['lat'],tmp['lon']=geo2lat(item[key])
                    map[geo]={'lat':tmp['lat'],'lon':tmp['lon']}
                elif geo in map:
                    tmp['lat']=map[geo]['lat']
                    tmp['lon']=map[geo]['lon']
                if key=='actor1geo_fullname':
                    tmp['color']='red'
                    tmp['name']=actor1name
                    tmp['geo'] = geo
                elif key=='actor2geo_fullname':
                    tmp['color']='blue'
                    tmp['name']=actor2name
                    tmp['geo'] = geo
                    #if item['actor1geo_fullname']!="null":
                    tmp['hub'] = item['actor1geo_fullname']
                key=key+'1'
                item[key]=tmp
    return dict

#dict={'total': 4, 'res': [{'sqldate': '20180502', 'sentid': '5ae994a9aacf802249155fb3_0', 'actor2geo_fullname': 'China', 'actor1geo_fullname': 'Canberra'}, {'sqldate': '20180502', 'sentid': '5ae994b3aacf802249155fc2_0', 'actor2geo_fullname': 'Beijing', 'actor1geo_fullname': 'Canberra'}, {'sqldate': '20180502', 'sentid': '5ae994a9aacf802249155fb6_0', 'actor2geo_fullname': 'China', 'actor1geo_fullname': 'Canberra'}, {'sqldate': '20180506', 'sentid': '5af29c05aacf80224916d1a7_1', 'actor2geo_fullname': 'China', 'actor1geo_fullname': 'Harare'}], 'actor1name': 'President', 'actor2name': 'China'}
#all_geo2lat(dict)
#print(all_geo2lat(event_combine_by_name('President','China11',55)))