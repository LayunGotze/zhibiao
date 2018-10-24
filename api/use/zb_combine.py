import json
dict1={}
dict2={}
with open('code1.0.txt','r') as f:
    dict1=json.loads(f.read())
    print(len(dict1))
for i in range(2,12):
    with open('code{num}.0.txt'.format(num=i),'r') as f:
        dict2={}
        dict2=json.loads(f.read())
        print(len(dict2))
    for key in dict2:
        if key not in dict1:
            dict1[key]=dict2[key]
        else:
            try:
                dict1[key]=list(set(dict2[key]+dict1[key]))
            except:
                pass

    print(len(dict1))
    print("  ")
with open('code12.2.txt','r') as f:
    dict2={}
    dict2=json.loads(f.read())
    print(len(dict2))
for key in dict2:
    if key not in dict1:
        dict1[key]=dict2[key]
    else:
        try:
            dict1[key]=list(set(dict2[key]+dict1[key]))
        except:
            pass

print(len(dict1))
print("  ")
with open('code.txt','w') as f:
    f.write(json.dumps(dict1))