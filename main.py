# -*- coding:utf-8 -*-
import hduReader
import mnnuReader
import RankListWriter
import LogWrite
import urllib2
import time
import traceback
import socket
import setting
import User


LOOP_SELLP_TIME = setting.Main_Loop_Interval  # 每次主循环的间隔时间


# 这里是主文件。用 python main.py 运行这个脚本
if __name__ == '__main__':
    # 准备写入日记
    LogWrite.log.start()
    print u"System Start!"
    LogWrite.log.log_wirte(u"System Start", info = True)
    is_first_run = True
    while True:
        if is_first_run == False:
            time.sleep(LOOP_SELLP_TIME)
            LogWrite.log.log_wirte(u"Begin the first loop.", info = True)
        else:
            is_first_run = False

        LogWrite.log.log_size_arrive_max()
        # 测试是否与HDU和MNNU连通
        try:
            request = urllib2.Request(setting.MNNU_Url)
            response = urllib2.urlopen(request, timeout = setting.Time_Out)
            print setting.MNNU_Url + u"Read succeed."
        except urllib2.URLError, e:
            info = str(setting.MNNU_Url).encode('utf-8') + u"Read error："
            if hasattr(e, "code"):
                info = info + u' ' + str(e.code).encode('utf-8')
            if hasattr(e, "reason"):
                info = info + u' ' + str(e.reason).encode('utf-8')
            print info
            LogWrite.log.log_wirte(info, error = True)
            continue
        except socket.timeout, e:
            info = str(setting.MNNU_Url).encode('utf-8') + u"Read out time："
            if hasattr(e, "code"):
                info = info + u' ' + str(e.code).encode('utf-8')
            if hasattr(e, "reason"):
                info = info + u' ' + str(e.reason).encode('utf-8')
            print info
            LogWrite.log.log_wirte(info, error = True)
            continue

        try:
            request = urllib2.Request(setting.HDU_Url,
                                      headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
            response = urllib2.urlopen(request, timeout = setting.Time_Out)
            print setting.HDU_Url + u"Read succeed"
        except urllib2.URLError, e:
            info = setting.HDU_Url + u"Read error："
            if hasattr(e, "code"):
                info = info + u' ' + str(e.code).encode('utf-8')
            if hasattr(e, "reason"):
                info = info + u' ' + str(e.reason).encode('utf-8')
            print info
            LogWrite.log.log_wirte(info, error = True)
            continue
        except socket.timeout, e:
            info = setting.HDU_Url + u"Read out time："
            if hasattr(e, "code"):
                info = info + u' ' + str(e.code).encode('utf-8')
            if hasattr(e, "reason"):
                info = info + u' ' + str(e.reason).encode('utf-8')
            print info
            LogWrite.log.log_wirte(info, error = True)
            continue

        try:
            print "Start try"
            # 由MMNUReader读取满足条件的用户
            mnnu_reader = mnnuReader.MNNU_Reader()
            users_list = mnnu_reader.read_users()
            # 接下去由hduReader来负责
            hdu_reader = hduReader.HDUReader()
            hdu_reader.get_user_info(users_list)
            # 结束hduReader作用

            # 排序
            users_list.sort()
            print u"Sort finish. Begin to write Rank List."
            LogWrite.log.log_wirte(u"Sort finish. Begin to write Rank List.", info = True)

            # 接下去RankListWriter类负责
            rank_list_writer = RankListWriter.RankListWrite()
            rank_list_writer.start()
            idx = 1
            for per_user in users_list:
                if per_user.is_legal == True:
                    per_item = [str(idx).encode('utf-8')]
                    if idx == 1:
                        per_item[0] = per_item[0] + u'<img src="images/gold.png" alt=""/>'
                    elif idx == 2:
                        per_item[0] = per_item[0] + u'<img src="images/silver.png" alt=""/>'
                    elif idx == 3:
                        per_item[0] = per_item[0] + u'<img src="images/copper.png" alt=""/>'
                    per_item.append(per_user.user_name)
                    per_item.append(per_user.nike_name)
                    per_item.append(per_user.moto)
                    per_item.append(str(per_user.solved_number))
                    per_item.append(str(per_user.submissions))
                    per_item.append(str(("%.2f" % per_user.ac_rate)).encode("utf-8"))
                    # print  per_item
                    rank_list_writer.write_tiem(per_item)
                    idx += 1
            # 结束
            rank_list_writer.end()
            print u"Rank list finish.Main Loop finish."
            LogWrite.log.log_wirte(u"Rank list finish.Main Loop finish.")
        except BaseException, e:
            traceback.print_exc()
            LogWrite.log.log_wirte(str(traceback.format_exc()).encode('utf-8'), error = True)
