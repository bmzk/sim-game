"""定义factory 类"""

import lib.gui as gui
import lib.function as fun
import lib.defines as df
import json
import time


class Factory(gui.MYGUI):
    def __init__(self) -> None:
        ## 常量 ########################
        self.worker_per_lv = 10
        """常量，每升一级可增加的工人数量"""
        self.need = {}
        """每单位生产消耗"""
        self.out = 9999
        """每人每天的产量"""
        self.type = ""
        """生产的产品类型"""
        self.name = ""
        """factory 的名字"""
        self.jf = "test.json"
        """json文件,"""
        ## 变量 ########################
        self.lv = 99999
        """等级，决定了最大工人数量"""
        # self.worker = 1
        """当前工人数量"""
        self.lv_up_need = []
        self.day = 0
        ## 用于显示的量 #############################
        self.count = 0
        """公共仓库中good的数量"""
        ##
        gui.MYGUI.__init__(self, _name=self.name)

    def get_data(self):
        """初次启动应调用。
        每当工厂有变动如工人数量、等级变更时才会调用，不应该每日循环"""
        try:
            with open(self.jf, "r") as f:
                data = json.load(f)
        except:
            data = {}
        self.lv = data.get("level", 1)
        self.worker = data.get("worker", 1)

    def set_data(self):
        """每当工厂有变动如工人数量、等级变更时才会调用，不应该每日循环"""
        data = {
            "level": self.lv,
            "worker": self.worker,
            "type": self.type,
        }
        with open(self.jf, "w") as f:
            json.dump(data, f)

    def day_sub(self):
        self.day = fun.get_day()
        print("==" * 20)
        time.sleep(1)
        print("day:", self.day)
        ## 读取数据 ############################################
        goods: dict = fun.get_user_data()

        ## 计算可购入的份数 ####################################
        """可购入的份数"""
        n = self.worker
        ## 更新物品数量 #######################################
        for i in self.need:
            goods.update({i: goods.get(i, 0) - n * self.need[i]})
        goods.update({self.type: goods.get(self.type, 0) + n * self.out})
        ##
        self.count = goods.get(self.type, 0) + n * self.out

        ## 增减工人数量
        if goods.get(i, 0) < 0 and self.worker < self.worker_per_lv * self.lv:
            self.worker = self.worker + 1
        elif goods.get(i, 0) > 10000 * self.lv and self.worker > 0:
            self.worker = self.worker - 1
        ## 写入数据 ############################################
        fun.set_user_data(goods)
        ##################################################
        self.display()

    def lv_change(self, k: int) -> None:
        ## 读取数据 ############################################
        goods: dict = fun.get_user_data()
        ## 更新物品数量 #######################################
        for i in self.lv_up_need:
            goods.update({i: goods.get(i, 0) - self.worker * self.lv_up_need[i] * k})
        ## 写入数据 ############################################
        fun.set_user_data(goods)
        ## 等级变更和写入数据 #############################
        self.lv = self.lv + k
        self.set_data()
        ###############################
        self.display()

    def woker_change(self, k):
        self.worker = self.worker + k
        self.set_data()
        self.display()

    def display(self):
        self.lab1_4.config(text=self.day)
        self.lab2_2.config(text=self.lv)
        self.lab3_4.config(text=self.worker_per_lv * self.lv)
        self.lab4_2.config(text=self.worker)

    def int_to_str(self):
        k = ""
        if self.count < 0:
            k = "-"
        rv = str(int(self.count)).replace("-", "")
        if len(rv) < 7:
            return k+rv
        elif len(rv)<10:
            return k+rv[:-6]+','+rv[-6:-3]+','+rv[-3:]
        else:
            return k+rv[:-9]+','+rv[-9:-6]+','+rv[-6:-3]+','+rv[-3:]

