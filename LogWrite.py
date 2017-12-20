# -*- coding:utf-8 -*-
import codecs
import time
import setting
import os
from os.path import getsize

######
#   写日记类
######

LOG_FILE = "Log.html"
LOG_MAX_SIZE = setting.Log_Size  # 日记最大值（以KB为单位）
LOG_SAVE_LINE = setting.Log_Save_Line  # 清空LOG后保留多少行


class LogWrite:
    # Log日记的网页头部
    __log_head__ = u'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <title>Log</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link href="log.css" rel="stylesheet" type="text/css">
</head>
<body>
'''

    # 初始化
    def __init__(self):
        self.log_file = codecs.open(LOG_FILE, 'w', 'utf-8')  # 修改过的

    # 开始启动
    def start(self):
        print "start"
        # 覆盖并生成新的日记
        self.log_file.write(self.__log_head__)

    # 写入日记
    def log_wirte(self, content, info = False, warm = False, error = False):
        if type(content) is type(""):
            content = content.decode('utf-8')
        if warm:  # 输出警告
            self.log_file.write(u'<p class="warm">[warm] ')
        elif error:  # 输出错误
            self.log_file.write(u'<p class="error">[error] ')
        else:  # 输出普通信息
            self.log_file.write(u'<p class="info">[info] ')
        # 写入时间
        str_time = time.strftime('%Y-%m-%d %X', time.localtime()).decode('utf-8')
        print type(str_time), type(content)
        str_content = str_time + u'&#09;' + content + u'</p>' + u"\n"
        # str_content=str_content.encode('utf-8')
        self.log_file.write(str_content)

    # 日记大小是否达到最大值，如果达到就清空
    def log_size_arrive_max(self):

        log_size = getsize(LOG_FILE)
        log_size = log_size / 1024  # 转换成KB
        if log_size > LOG_MAX_SIZE:
            # 获取最后几行的LIST
            print "Log arrive max size."
            self.log_file.close()
            self.log_file = codecs.open(LOG_FILE, encoding = 'utf-8')
            str_buff_list = []
            self.log_pos = 0
            for line in range(LOG_SAVE_LINE):
                str_lastline = self.lastline()
                str_buff_list.append(str_lastline)
            self.log_file.close()

            # 开始写入
            self.log_file = codecs.open(LOG_FILE, 'w', 'utf-8')
            self.log_file.seek(0, 0)
            self.log_file.write(self.__log_head__)
            while str_buff_list:
                self.log_file.write(str_buff_list.pop())

    # 从倒数开始取起
    def lastline(self):
        while True:
            self.log_pos = self.log_pos - 1
            try:
                self.log_file.seek(self.log_pos, 2)
                tttchar = self.log_file.read(1)
                if tttchar == "\n":
                    break
            except:  # 异常处理
                self.log_pos = self.log_pos - 1
        strs = self.log_file.readline()
        print strs
        return strs


# 生成实例
log = LogWrite()
