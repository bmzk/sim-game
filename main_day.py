import lib.function
import json
import time
# json文件
jf='data/common.json'


while True:
    time.sleep(1.5)
    print('=='*20)
    try:
        with open(jf, 'r') as f:data = json.load(f)
        print('data old:',data)
    except json.JSONDecodeError:
        data={}
    try:
        day = data['day']
        print('day:',day)
    except KeyError:
        print('data中没有day   data：',data)
        data.update({'day':0})
        day=0

    day=day+1
    data.update({'day':day})
    print('data new:',data)
    with  open(jf, 'w') as f:json.dump(data, f)
    print()

