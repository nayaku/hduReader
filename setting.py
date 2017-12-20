# -*- coding:utf-8 -*-
import time
import datetime

######
#   设置区域
######

# 重试时间(s)
Time_Out = 10
###### 主函数控制区域
# 主循环间隔时间(s)
Main_Loop_Interval = 500

###### 读取MNNU控制区域
# MNNU读取循环间隔时间(s)
MNNU_Loop_Interval = 0.8  # 0.8
# MNNU的网址
MNNU_Url = 'http://acm.mnnu.edu.cn'
# 新生排名页面
MNNU_Ranklist = 'http://acm.mnnu.edu.cn/index.php/User/novice/p/'

###### 读取hdu控制区域
# HDU循环间隔时间(s)
HDU_Loop_Interval = 1#1
# HDU的网址
HDU_Url = 'http://acm.hdu.edu.cn'
# HDU用户读取页面
HDU_User_Url = 'http://acm.hdu.edu.cn/userstatus.php?user='
# 最早合法账号的注册时间
Earliest_Register_Date = datetime.datetime(2012, 6, 1)

###### 排行页面显示控制区域
# 排行页面的注释
Note = u'''

'''

###### 日记控制区域
# 日记大小(kb)
Log_Size = 128
# 清空日记后日记保留的行数
Log_Save_Line = 30
