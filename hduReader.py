# -*- coding:utf-8 -*-
import urllib2
import re
import LogWrite
import time
import datetime
import User
import setting

HDU_URL = setting.HDU_Url  # HDU的地址
SLEEP_TIME = setting.HDU_Loop_Interval  # 在HDU上面读取循环间隔时间
Earliest_Registed_Date = datetime.datetime(2016,6,1)   #最早合法账号的注册时间

# TEMP_USER = '736248591'  #爬虫临时使用的用户名
######
#   HDU读取类
######
class HDUReader:
    __hdu_url__ = setting.HDU_User_Url

    # 获取用户信息
    def get_user_info(self, user_list):
        for i in range(len(user_list)):
            user_name = user_list[i].user_name
            url = self.__hdu_url__ + user_name
            print url
            try:
                user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                headers = {'User-Agent': user_agent}
                request = urllib2.Request(url, headers = headers)
                response = urllib2.urlopen(request, timeout = setting.Time_Out)
                # print response.read().decode("gbk").encode("utf-8")
                content = response.read().decode("gbk").encode("utf-8")
                content = unicode(content, "utf-8")  # 貌似上面的不行，这里强行转换
                items = self.math_string(content)
                for item in items:  # 迭代每个匹配到的项目
                    t_str = u"在HDUOJ上成功完成" + user_name + u"的读取。"
                    print t_str
                    LogWrite.log.log_wirte(t_str, info = True)

                    user_registed_time=datetime.datetime.strptime(item[0],"%Y-%m-%d")
                    if user_registed_time<Earliest_Registed_Date:
                        user_list[i].is_legal=False
                        t_str=user_name+u"不在指定的创建日期内。"
                        print t_str
                        LogWrite.log.log_wirte(t_str,warm = True)
                    else:
                        user_list[i].moto = item[1]
                        user_list[i].solved_number = int(item[2])
                        user_list[i].submissions = int(item[3])
                        if float(item[3]) != 0.0:
                            user_list[i].ac_rate = float(item[2]) * 100.0 / float(item[3])
                        else:
                            user_list[i].ac_rate = 0.0
                        time.sleep(SLEEP_TIME)
            except urllib2.URLError, e:
                if hasattr(e, "code"):
                    print e.code
                    LogWrite.log.log_wirte(str(e.code).encode('utf-8'), error = True)
                if hasattr(e, "reason"):
                    print e.reason
                    LogWrite.log.log_wirte(str(e.reason).encode('utf-8'), error = True)

    # 开始匹配
    def math_string(self, content):
        pattern = re.compile(
            'registered on (.*?)</i>.*?'+
            '<p>(.*?)</p>.*?' +
            '<tr><td>Problems Solved</td><td align=center>(.*?)</td></tr>.*?' +
            '<tr><td>Submissions</td><td align=center>(.*?)</td></tr>', re.S)  # 正则表达式
        items = re.findall(pattern, content)
        return items

# CLASS运作测试
# hdu_reader = HDUReader()
# hdu_reader.get_user_info(TEMP_USER)
