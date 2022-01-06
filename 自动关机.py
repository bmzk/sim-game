import math
import os
import threading
import time
import winsound

import wx


def timestr():
    '''获取指定格式的时间'''
    rv=time.strftime("%H:%M:%S", time.localtime()) 
    rv=rv+'::'+str(int((time.time()-int(time.time()))*1000))
    return rv

class Mywin(wx.Frame):
    '''创建一个窗口类.\n'''
    def __init__(self):
        ''' 构造函数'''
        super(Mywin, self).__init__(None, title='自动关机', size=(600, 400))
        ############################################################
        self.grid = wx.BoxSizer(wx.VERTICAL) 
        self.panel = wx.Panel(self)
        ###########################################################
        self.lasttime=0
        self.endtime=time.time()+5000
        self.isshutdowning=False
        #
        print('# self.Show()')
        self.addctrls(self.panel,self.grid)
        #
        self.creat_timer()

        print(1)

        #self.statusBar.Add()
        self.panel.SetSizerAndFit(self.grid)
        self.Center()
        #self.timerdef(0.02)
        self.Show()
    def creat_timer(self):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.timerdef,self.timer)
        self.timer.Start(250,False)
        #
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.timerdef2,self.timer2)
        self.timer2.Start(50,False)

    def addctrls(self,panel,grid):
        self.addbox1( panel,grid)
        self.fgx()
        ##############################################################
        self.endtime_label=wx.StaticText(self.panel,style=wx.ALIGN_CENTER,
            label='关机时间：00时00分00秒')
        self.endtime_label.SetForegroundColour(wx.RED)
        self.endtime_label.SetBackgroundColour(wx.BLACK)
        font = wx.Font(35, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.NORMAL) 
        self.endtime_label.SetFont(font)
        self.grid.Add(self.endtime_label,flag=wx.CENTER)
        self.fgx()
        #####################################
        self.addbox2( panel,grid)
        self.fgx(3)
        #########################################
        self.addbox3( panel,grid)
        self.fgx()
        #########################################
        self.addbox4( panel,grid)
        self.fgx()
        ## 添加状态栏 ########################################
        self.addstatusbar()
        ##
        #self.addmenubar()
    def addstatusbar(self):
        self.statusBar = self.CreateStatusBar(2)
        self.statusBar.Label='状态栏'
        
        #
    def addmenubar(self):
        self.menubar=wx.MenuBar()
        self.menu1=wx.Menu('静音')
        #self.audio=wx.CheckBox(self.panel,label='静音')
        self.menu1.AppendCheckItem(-1,'00')
        self.menubar.Append(self.menu1,'设置')
        self.SetMenuBar( self.menubar)
        #Append(self.audio)
    def addbox1(self, panel,grid):
        '''窗口第一行，显示模式选择和本地时间'''
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.NORMAL) 
        # 容器
        self.box1=wx.BoxSizer(wx.HORIZONTAL)
        # 控件1
        self.rb1 = wx.RadioButton(panel,label = '倒计时模式') 
        self.rb1.SetValue(True)
        self.rb1.SetFont(font)
        self.box1.Add(self.rb1)
        # 控件2
        self.rb2 = wx.RadioButton(panel,label = '定时模式') 
        self.rb2.SetFont(font)
        self.box1.Add(self.rb2)
        # 控件3
        w=wx.StaticText(panel)
        #w.SetBackgroundColour(wx.BLACK)
        self.box1.Add(w,1,flag=wx.ALL|wx.EXPAND)
        # 控件4
        label_localtime = wx.StaticText(panel,label = '本地时间：') 
        label_localtime.SetFont(font)
        self.box1.Add(label_localtime)
        # 控件5
        self.localtime = wx.StaticText(panel,label = time.strftime("%H:%M:%S", time.localtime())) 
        self.localtime.SetFont(font)
        self.localtime.SetBackgroundColour((200,200,200))
        #localtime.SetForegroundColour((100,0,0)) 
        self.box1.Add(self.localtime)
        # 控件6
        font2 = wx.Font(14, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.NORMAL) 
        self.localtime2 = wx.StaticText(panel,label = '::'+str(int((time.time()-int(time.time()))*1000)))
        self.localtime2.SetFont(font2)
        self.localtime2.SetBackgroundColour((200,200,200))
        self.localtime2.SetForegroundColour((255,0,0)) 
        self.box1.Add(self.localtime2)
        # 添加到面板
        grid.Add(self.box1,flag=wx.EXPAND)
        # 绑定事件
        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.bindingevent_rb) 
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.bindingevent_rb) 

    def addbox2(self, panel,grid):
        self.box2=wx.BoxSizer(wx.HORIZONTAL)
        self.box2.Add(wx.StaticText(panel),1,flag=wx.EXPAND)
        self.h=t(panel,self.box2)
        self.m=t(panel,self.box2)
        self.s=t(panel,self.box2)
        self.box2.Add(wx.StaticText(panel),1,flag=wx.EXPAND)
        grid.Add(self.box2,flag=wx.EXPAND)
        # binding
        self.h.bt_up.Bind(wx.EVT_BUTTON, self.bindingevent_bt1) 
        self.h.bt_down.Bind(wx.EVT_BUTTON, self.bindingevent_bt2) 
        self.m.bt_up.Bind(wx.EVT_BUTTON, self.bindingevent_bt3) 
        self.m.bt_down.Bind(wx.EVT_BUTTON, self.bindingevent_bt4) 
        self.s.bt_up.Bind(wx.EVT_BUTTON, self.bindingevent_bt5) 
        self.s.bt_down.Bind(wx.EVT_BUTTON, self.bindingevent_bt6) 

    def addbox3(self, panel,grid):
        self.gauge=wx.Gauge(panel)
        self.gauge.BackgroundColour=wx.BLACK
        self.gauge.ForegroundColour=wx.RED
        self.gauge.Value=50
        self.gauge.Pulse()
        grid.Add(self.gauge,flag=wx.EXPAND)

        self.gauge_label=wx.StaticText(self.panel,label='20/100',style=wx.ALIGN_CENTER)
        #self.gauge_label.SetBackgroundColour(colour=wx.BLUE)
        #self.gauge_label.SetPosition((self.Size[0]*0.5,self.gauge.GetPosition()[1]))
        grid.Add(self.gauge_label,flag=wx.CENTER)

    def addbox4(self, panel,grid):
        font2 = wx.Font(30, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        self.bt=wx.Button(panel,label='开 始',size=(250,80))
        self.bt.SetFont(font2)
        grid.Add(self.bt,flag=wx.CENTER)
        self.bt.Bind(wx.EVT_BUTTON, self.bindingevent_bt) 

    def fgx(self,n:'权重'=10):
        '''分割线'''
        st=wx.StaticText(self.panel)
        #st1.SetBackgroundColour(colour=wx.YELLOW)
        self.grid.Add(st,1,flag=wx.EXPAND)

    def bindingevent_bt(self,event):
        if self.lasttime<15:
            #a=wx.Dialog(self.panel,title='78979')
            self.lasttime=15
        if self.bt.Label=='开 始':

            self.isshutdowning=True
            self.bt.Label='暂 停'
            self.gauge.Range=self.lasttime
            self.disablectrls(False)
        else:
            self.isshutdowning=False
            self.bt.Label='开 始'
            self.disablectrls(True)

    def disablectrls(self,boolvalue=True):
        self.rb1.Enabled=boolvalue
        self.rb2.Enabled=boolvalue
        self.h.bt_up.Enabled=boolvalue
        self.h.bt_down.Enabled=boolvalue
        self.m.bt_up.Enabled=boolvalue
        self.m.bt_down.Enabled=boolvalue
        self.s.bt_up.Enabled=boolvalue
        self.s.bt_down.Enabled=boolvalue

    def bindingevent_rb(self,event):
        #if self.rb1.Value:
        self.lasttime=0
        self.endtime=time.time()
        
    def bingevent_bt_use(self,k=1,n=3600):
        '''k：点击向上按钮k=1，点击向下按钮k=-1\n
        n：每次点击增加或减少的数值'''
        if self.rb1.Value:
            self.lasttime += k*n
            self.endtime=self.lasttime+time.time()
        elif self.rb2.Value:
            self.endtime += k*n
        if self.lasttime < 0:
            self.lasttime = 0
        #
        self.gauge.SetRange(self.lasttime)
        # 发声音
        f=int(math.log10(n))*500+500+k*100
        print(f)
        winsound.Beep(f,150)

    def bindingevent_bt1(self,event):
        self.bingevent_bt_use(1,3600)
        print('press',self,type(self),self.Id,self.Name,event)
        #if 
    def bindingevent_bt2(self,event):
        self.bingevent_bt_use(-1,3600)
        print('press',self,type(self),self.Id,self.Name)
    def bindingevent_bt3(self,event):
        self.bingevent_bt_use(1,60)
    def bindingevent_bt4(self,event):
        self.bingevent_bt_use(-1,60)
    def bindingevent_bt5(self,event):
        self.bingevent_bt_use(1,1)
    def bindingevent_bt6(self,event):
        self.bingevent_bt_use(-1,1)

    
    def timerdef(self,intever=0.2):
        '''定时器事件'''
        # 更新关机时间
        self.endtime_label.Label='关机时间：'+time.strftime("%H:%M:%S", time.localtime(self.endtime))
        print(self.endtime_label.Label)
        # 更新倒计时

        if self.isshutdowning:
            self.lasttime=self.endtime-time.time()
            t=self.lasttime
            if t<1:
                os.system('shutdown -s -t 1')
                t=0
        else:
            #self.endtime = self.lasttime+time.time()
            if self.rb1.Value:
                t=self.lasttime
                self.endtime = self.lasttime+time.time()
            if self.rb2.Value:
                t=time.localtime(self.endtime)[3]*3600+time.localtime(self.endtime)[4]*60+time.localtime(self.endtime)[5]
        
        try:
            v=self.gauge.GetRange()-self.lasttime
            self.gauge.SetValue(v)
            self.gauge_label.SetLabel(str(int(100*v/self.gauge.GetRange()))+'/100')
        except :
            pass

        self.h.st.Label=self.int_str(self.n_timestr(t)[0])+'时'
        self.m.st.Label=self.int_str(self.n_timestr(t)[1])+'分'
        self.s.st.Label=self.int_str(self.n_timestr(t)[2])+'秒'
        #print('threading.active_count()',threading.active_count())
    def n_timestr(self,t):
        '''将一个数字转换为时分秒表示形式'''
        t=int(t)
        h=t//3600
        m=(t-h*3600)//60
        s=t%60
        return (h,m,s)
    def int_str(self,n):
        n=int(n)
        if n<10:
            rv='0'+str(n)
        else:
            rv=str(n)
        return rv

    def timerdef2(self,intever=0.2):
        '''定时器事件'''
        # 更新本地时间
        self.localtime.Label=time.strftime("%H:%M:%S", time.localtime())
        global ms
        ms=int((time.time()%1)*1000)
        if ms<10:
            self.localtime2.Label = '::00'+str(ms)
        elif ms<100:
            self.localtime2.Label = '::0'+str(ms)
        else :
            self.localtime2.Label = '::'+str(ms)
        print('threading.active_count()',threading.active_count())
 


class t(object):
    def __init__(self,panel,grid):
        sizer=wx.GridBagSizer()

        font1 = wx.Font(40, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        self.st=wx.StaticText(panel,style=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT,label='00分',size=(130,30))
        self.st.SetFont(font1)
        self.st.SetBackgroundColour((220,220,220))
        sizer.Add(self.st,pos=(0,0),span=(2,1),flag=wx.EXPAND)

        font2 = wx.Font(25, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        self.bt_up=wx.Button(panel,label='+',size=(30,30),name='jia')
        self.bt_up.SetFont(font2)
        sizer.Add(self.bt_up,pos=(0,1))
        
        self.bt_down=wx.Button(panel,label='-',size=(30,30),name='jian')
        self.bt_down.SetFont(font2)
        sizer.Add(self.bt_down,pos=(1,1))

        grid.Add(sizer)

def 启动窗口():
    app = wx.App()
    win = Mywin()
    app.MainLoop()

启动窗口()
