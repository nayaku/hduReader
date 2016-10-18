# -*- coding:utf-8 -*-
import time
import datetime

######
#   设置区域
######

# 重试时间(s)
Time_Out = 3
###### 主函数控制区域
# 主循环间隔时间(s)
Main_Loop_Interval = 180

###### 读取MNNU控制区域
# MNNU读取循环间隔时间(s)
MNNU_Loop_Interval = 0.8
# MNNU的网址
MNNU_Url = 'http://acm.mnnu.edu.cn'
# 新生排名页面
MNNU_Ranklist = 'http://acm.mnnu.edu.cn/index.php/User/novice/p/'

###### 读取hdu控制区域
# HDU循环间隔时间(s)
HDU_Loop_Interval = 1
# HDU的网址
HDU_Url = 'http://acm.mnnu.edu.cn'
# HDU用户读取页面
HDU_User_Url = 'http://acm.hdu.edu.cn/userstatus.php?user='
# 最早合法账号的注册时间
Earliest_Register_Date = datetime.datetime(2016, 6, 1)

###### 排行页面显示控制区域
# 排行页面的注释
Note = u'''
        &nbsp;&nbsp;在大一上学期的10月22日、11月12日，ACM队将在我校OJ(acm.mnnu.edu.cn)举办两场网络赛，只要在这两场网络赛中的其中一场获得前十五名的名次，就可直接获得12月8日举行的现场赛的参赛资格。除了在网络赛获得名次外，还可以通过杭电OJ(acm.hdu.edu.cn)做题数达标来获取入围现场赛的资格，入围的标准是男生80题，女生65题。现场赛结束后，我们会综合考虑之前每场比赛和练习的情况，确认入队名单。
        <br/>
        &nbsp;&nbsp;入队后将会有一星期2次的教学和练习。地点在励志楼311。同时寒暑假也会有适当的练习。等水平上来了有实力了就可以外出比赛拿奖了。
        <br/>
        &nbsp;&nbsp;可以加下群：<a href="http://jq.qq.com/?_wv=1027&k=40A1v8F">575224728</a>。你们问问题的同时也方便我们通知一些事情。
'''

###### 日记控制区域
# 日记大小(kb)
Log_Size = 128
# 清空日记后日记保留的行数
Log_Save_Line = 30
