# -*- coding:utf-8 -*-
import time
import urllib2
import re
import User
import LogWrite
import setting

MNNU_URL = setting.MNNU_Url  # MNNUOJ地址
SLEEP_TIME = setting.MNNU_Loop_Interval  # 爬入下一个页面的时间


######
#   HDU读取类
######
class MNNU_Reader:
    __users_url__ = setting.MNNU_Ranklist  # 抓取页面

    # 读取满足条件的用户
    def read_users(self):
        users_list = []
        try:
            for page in range(1, self.get_pages_number()):
                content = self.read_page(self.__users_url__ + str(page))
                pattern = re.compile("<a href='/User/info/username/(.*?)'>", re.S)
                items = re.findall(pattern, content)
                print "Read each user"
                for item in items:
                    print item
                    # 进入用户信息页面，二次匹配
                    user_url = MNNU_URL + '/User/info/username/' + item
                    content = self.read_page(user_url)
                    pattern = re.compile(u'<div class="username">(.*?)</div>.*?杭电账号=&.*?;(.*?)&', re.S)
                    new_item = re.findall(pattern, content)
                    if new_item and new_item[0]:
                        # 添加到用户列表
                        new_hdu_user = User.User(new_item[0][1])
                        new_hdu_user.nike_name = new_item[0][0]
                        users_list.append(new_hdu_user)

                        #
                        # newitem = item[1].replace("<br />", "")
                        # newitem = re.sub('<.*?>|</.*?>', "", newitem)
                        # newitem = re.sub('<tr>|<div>|</div>|</p>', "\t", newitem)
                        # newitem = re.sub("\n", '', newitem)

                        # 二次匹配
                        # second_pattern = re.compile(u'杭电账号=&.*?;(.*?)&.*?;', re.S)
                        # second_item = re.findall(second_pattern, newitem)
                        # if second_item and isinstance(second_item[0], (str, unicode)):
                        #     user_name = item[0]
                        #     user_name = user_name.replace(" ", '')
                        #     user_name = user_name.replace("\t", '')
                        #
                        #     # 写日记
                        #     t_str = u"In MNNUOJ上成功读取到" + user_name + u"用户的信息！"
                        #     LogWrite.log.log_wirte(t_str)
                        #     print t_str
                        #
                        #     new_hdu_user = User.User(second_item[0])
                        #     new_hdu_user.nike_name = user_name
                        #     users_list.append(new_hdu_user)
        # 异常处理
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
                LogWrite.log.log_wirte(str(e.code).decode('utf-8'), error=True)
            if hasattr(e, "reason"):
                print e.reason
                LogWrite.log.log_wirte(str(e.reason).decode('utf-8'), error=True)
        return users_list

    # 连接到页面，并返回页面内容
    def read_page(self, page_url):
        time.sleep(SLEEP_TIME)
        t_str = "Read page: " + str(page_url)
        LogWrite.log.log_wirte(t_str, info=True)
        print t_str
        request = urllib2.Request(page_url)
        response = urllib2.urlopen(request, timeout=setting.Time_Out)
        contemt = response.read().decode("utf-8", "ignore")
        return contemt

    # 获取页面的数量
    def get_pages_number(self):
        url = setting.MNNU_Ranklist + '1'
        content = self.read_page(url)
        pattern = re.compile("class='last' >... (.*?)</a>", re.S)
        pages_number = int(re.findall(pattern, content)[0])
        return pages_number
