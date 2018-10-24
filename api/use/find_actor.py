from api.use.mongodb_link import events_tracking

def find_actor1_events(actor1name="null",actor1code="null"):
    #根据ACTOR1的名称或CODE搜索与其有关的事件CODE及对应动词
    #list=find_actor1_events(actor1code="CHN",actor1name="President")
    event_code_list={}
    search_key={}
    if actor1name!="null" and actor1code=="null":
        search_key={"actor1name": actor1name}
    elif actor1name=="null" and actor1code!="null":
        search_key={"actor1code": actor1code}
    elif actor1name!="null" and actor1code!="null":
        search_key={"actor1name": actor1name,"actor1code": actor1code}
    tmp=events_tracking.find(search_key)
    for item in tmp:
        if 'eventcode' in item:
            if 'eventcode' not in event_code_list:
                if 'eventverb' not in item:
                    event_code_list[item['eventcode']]=[]
                else:
                    event_code_list[item['eventcode']]=[item['eventverb']]
            else:
                if 'eventverb' in item:#缺少list去重
                    event_code_list[item['eventcode']].append(item['eventverb'])
    return event_code_list

def find_actor2_events(actor2name="null",actor2code="null"):
    #根据ACTOR2的名称或CODE搜索与其有关的事件CODE及对应动词
    #list=find_actor2_events(actor2code="CHN",actor2name="President")
    event_code_list={}
    search_key={}
    if actor2name!="null" and actor2code=="null":
        search_key={"actor2name": actor2name}
    elif actor2name=="null" and actor2code!="null":
        search_key={"actor2code": actor2code}
    elif actor2name!="null" and actor2code!="null":
        search_key={"actor2name": actor2name,"actor2code": actor2code}
    tmp=events_tracking.find(search_key)
    for item in tmp:
        if 'eventcode' in item:
            if 'eventcode' not in event_code_list:
                if 'eventverb' not in item:
                    event_code_list[item['eventcode']]=[]
                else:
                    event_code_list[item['eventcode']]=[item['eventverb']]
            else:
                if 'eventverb' in item:#缺少list去重
                    event_code_list[item['eventcode']].append(item['eventverb'])
    return event_code_list

