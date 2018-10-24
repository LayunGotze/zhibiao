import pymongo
import re
import json
client=pymongo.MongoClient(host='111.205.121.89',port=14201)
db=client.en_event
db.authenticate("gyc", "123456")
events_tracking=db.events_tracking

dict={}
code1_list=['actor1knowngroupcode','actor1type3code','actor1type1code','actor1code','actor1type2code','actor1countrycode']
code2_list=['actor2knowngroupcode','actor2type3code','actor2type1code','actor2code','actor2type2code','actor2countrycode']

start=1200000
end=start+20000
cor=events_tracking.find().skip(start)
cnt=start

while cnt<end:
    print(cnt)
    cnt=cnt+1
    item=cor.next()
    if item['actor1name']=='' and item['actor2name']=='':
        continue
    #print(item['actor1name']+"   "+item['actor2name'])
    if item['actor1name']!='':
        tmp_list=[]
        for name in code1_list:
            if item[name]!='' and item[name] not in tmp_list:
                tmp_list.append(item[name])
        if item['actor1name'] not in dict:
            dict[item['actor1name']]=tmp_list
        elif item['actor1name'] in dict:
            for name in tmp_list:
                if name not in dict[item['actor1name']]:
                    dict[item['actor1name']].append(name)
    if item['actor2name']!='':
        tmp_list=[]
        for name in code2_list:
            if item[name]!='' and item[name] not in tmp_list:
                tmp_list.append(item[name])
        if item['actor2name'] not in dict:
            dict[item['actor2name']]=tmp_list
        elif item['actor2name'] in dict:
            for name in tmp_list:
                if name not in dict[item['actor2name']]:
                    dict[item['actor2name']].append(name)

with open('code{num}.txt'.format(num=end / 100000), 'w') as f:
    f.write(json.dumps(dict))
