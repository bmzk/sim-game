import json

# json文件
jf='data/common.json'


def get_day():
    with open(jf, 'r') as f:data = json.load(f)
    return data['day']