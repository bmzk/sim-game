#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk

import threading

class MYGUI:
    def __init__(self, _name="Factory") -> None:
        self.temp = 0 #测试用的数据
        ###################################################
        self.app = tk.Tk()
        self.app.title("my GUI")
        ###############
        self.lab1_0 = tk.Label(self.app, width=1)  # ,bg='#FF0099')
        self.lab1_0.grid(row=1, column=0)
        self.lab1_1 = tk.Label(self.app, text="名称")
        self.lab1_1.grid(row=1, column=1)
        self.lab1_2 = tk.Label(self.app, text=_name, fg="#FF0099")
        self.lab1_2.grid(row=1, column=2)
        self.lab1_4 = tk.Label(self.app, fg='#990000')
        self.lab1_4.grid(row=1, column=4)
        self.lab1_5 = tk.Label(self.app, text='天')  
        self.lab1_5.grid(row=1, column=5)
        ###########
        lab2_1 = tk.Label(self.app, text="等级")
        lab2_1.grid(row=2, column=1)
        self.lab2_2 = tk.Label(self.app, text=self.temp, fg="#FF0099")
        self.lab2_2.grid(row=2, column=2)
        self.lab2_3 = tk.Button(self.app, text="降级", command=lambda:self.lv_change(-1))
        self.lab2_3.grid(row=2, column=3)
        self.lab2_4 = tk.Button(self.app, text="升级", command=lambda:self.lv_change(1))
        self.lab2_4.grid(row=2, column=4)
        ###########
        lab3_1 = tk.Label(self.app, text="工人", height=2)  # ,border=3)
        lab3_1.grid(row=3, column=1)
        self.lab3_3 = tk.Label(self.app, text="最大数量")
        self.lab3_3.grid(row=3, column=3)
        self.lab3_4 = tk.Label(self.app, text=self.temp, fg="#FF0099")
        self.lab3_4.grid(row=3, column=4)
        ####################
        lab4_1 = tk.Label(self.app, text="当前数量")  # ,border=3)
        lab4_1.grid(row=4, column=1)
        self.lab4_2 = tk.Label(self.app, text=self.temp, fg="#FF0099")
        self.lab4_2.grid(row=4, column=2)
        self.lab4_3 = tk.Button(self.app, text="减少", command=lambda:self.woker_change(-1))
        self.lab4_3.grid(row=4, column=3)
        self.lab4_4 = tk.Button(self.app, text="增加", command=lambda:self.woker_change(1))
        self.lab4_4.grid(row=4, column=4)

        ############
        self.lab5_5 = tk.Label(self.app, width=5, height=1)  # ,bg='#FF0099')
        self.lab5_5.grid(row=5, column=5)
        ########################################
        #self.lab4_4.bind('<Button-1>',self.lv_change)
    def lv_change(self,k:int)->None:
        self.temp = self.temp+k
        print("this is level change: ", self.temp)

    def woker_change(self,k):
        '''测试用，使用时需要重构'''
        self.temp = self.temp + k
        self.display()
        print("this is change worker ", self.temp)



    def display(self):
        '''测试用，使用时需要重构'''
        self.lab1_4.config(text=self.temp)
        self.lab2_2.config(text=self.temp*2)
        self.lab3_4.config(text=self.temp*10)
        self.lab4_2.config(text=self.temp*5)

# threading.Thread(target=run, args=("t1",)).start()

if __name__=='__main__':
    '''测试用'''
    app = MYGUI()
    app.app.mainloop()


