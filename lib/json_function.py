'''读写JSON文件'''
import json


data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}


# json文件
jf='data/test/test.json'


# 写入一个json数据
with  open(jf, 'w') as f:json.dump(data, f)

with open(jf, 'r') as f:data2 = json.load(f)
print(data2)
