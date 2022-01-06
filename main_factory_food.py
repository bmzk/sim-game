''''''
from abc import abstractmethod
import time
import json
import lib.factory_class
import lib.function
import math
# json文件
jf = 'data/factory/food_factory.json'
default_price = {'food': 5, 'wood': 6, 'stone': 10, 'iron': 10}

'''商品的基础价格'''


class Factory():
    def __init__(self) -> None:
        ## 常量 ########################
        self.worker_per_lv = 1
        '''常量，每升一级可增加的工人数量'''
        self.need = {}
        '''每单位生产消耗'''
        self.out = 1
        '''每人每天的产量'''
        self.type = ''
        '''生产的产品类型'''
        self.name = ''
        '''factory 的名字'''
        self.jf = 'test.json'
        '''json文件,'''
        ## 变量 ########################
        self.level = 0
        '''等级，决定了最大工人数量'''
        self.worker = 1
        '''当前工人数量'''

        ## 用于显示的量 #############################
        self.money = 0
        self.count = 0
        self.price = 0
        pass
        ##

    def get_data(self):
        '''初次启动应调用。
        每当工厂有变动如工人数量、等级变更时才会调用，不应该每日循环'''
        try:
            with open(jf, 'r') as f:
                data = json.load(f)
        except:
            data = {}
        self.level = data.get('level', 1)
        self.worker = data.get('worker', 1)

    def set_data(self):
        '''每当工厂有变动如工人数量、等级变更时才会调用，不应该每日循环'''
        data = {
            'name': self.name,
            'level': self.level,
            'worker': self.worker,
            'type': self.type
        }
        with open(jf, 'w') as f:
            json.dump(data, f)

    def day_sub(self):
        ## 读取数据 ############################################
        try:
            with open('data/goods.json', 'r') as f:
                goods = json.load(f)
                '''各种商品的数量'''
        except:
            goods = {}
        try:
            with open('data/price.json', 'r') as f:
                price = json.load(f)
        except:
            price = {}
        try:
            with open('data/money.json', 'r') as f:
                money = json.load(f)
        except:
           money = {}
        ##############################################
        # 购买物品
        m = 0
        '''每单位购入需要的钱'''
        for i in self.need:
            p = price.get(i, default_price[i])
            m = m+p* self.need[i]
        self.money=money.get(self.type,10000)
        n = int(self.money/m)
        n = min(n, self.worker)
        print('购入','数量',n,'成本', m)
        for i in self.need:
            goods.update({i: goods.get(i, 0)-n*self.need[i]})
        goods.update({self.type: goods.get(self.type, 0)+n*self.out})
        self.count =  goods.get(self.type, 0)+n*self.out
        money.update({self.type: money.get(self.type, 10000)-n*m})
        for i in default_price:
            if goods.get(i, 0) <0 :
                price.update({i:price.get(i,default_price[i])*1.01})
            else:
                 price.update({i:price.get(i,default_price[i])*0.99})
        self.price=price.get(self.type,default_price[i])
        ## 写入数据 ############################################
        with open('data/goods.json', 'w') as f: json.dump(goods, f)
        with open('data/price.json', 'w') as f: json.dump(price, f)
        with open('data/money.json', 'w') as f: json.dump(money, f)


fac = Factory()
fac.worker_per_lv = 10
fac.need = {'wood': 2, 'stone': 1}
fac.out = 10
fac.type = 'food'
fac.name = 'Food Factory'
fac.jf = 'data/factory/food_factory.json'
fac.get_data()

while True:
    print('=='*20)
    time.sleep(1)
    t = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())
    print(t)
    print('day:',  lib.function.get_day())
    ##################################################
    fac.day_sub()
    print('money: {:.2f}'.format(fac.money),' count ',fac.count ,'price: {:.4f}'.format(fac.price))
    print()
