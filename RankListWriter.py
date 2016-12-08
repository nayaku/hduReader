# -*- coding:utf-8 -*-
import codecs
import time
import User
import shutil
import setting

######
#   HDU排名网页写入
######
TEMP_FILE_NAME = "TEMP_HDU_RANK_LIST.html"  # 临时文件名字
FILE_NAME = "HDU_RANK_LIST.html"  # 最终文件名字


class RankListWrite:
    # 开始写入
    def start(self):
        self.rank_file = codecs.open(TEMP_FILE_NAME, "w", "utf-8")  # 开始和要写入的文件挂钩
        self.rank_file.write(u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <script src="FindContent.js"></script>
    <link href="table_styles.css" rel="stylesheet" type="text/css"/>
    <link href="footer.css" rel="stylesheet" type="text/css"/>
    <title>HDU排行榜</title>
    <link rel="shortcut icon" href="images/LOGO_64x64.ico"/>
</head>
<body>
<div id="container">
<h1 style="text-align:center;">HDU 排名</h1>
<div><p>&nbsp;&nbsp;Search:<input name="key" style="width: 200px" type="text" id="key" onkeydown="onSearch(this,'mytable')" value=""/></p></div>
<table id="mytable" cellspacing="0" style="margin:auto ;width: auto">
''')
        str_time = time.strftime('%Y-%m-%d %X', time.localtime()).encode('utf-8')
        str_time = u'    <caption>Update at ' + str_time + u' </caption>'
        self.rank_file.write(str_time)
        self.rank_file.write(u'''
    <tr>
        <td>Rank</td>
        <td>User Name</td>
        <td>Nikename</td>
        <td>Moto</td>
        <td>Solved</td>
        <td>Submission</td>
        <td>Rate</td>
    </tr>
''')

    # 写入条目
    def write_tiem(self, item):
        self.rank_file.write(u'<tr>')
        for pitem in item:
            self.rank_file.write(u'<td>')
            str_pitem = pitem
            str_pitem = str_pitem.encode('utf-8')
            self.rank_file.write(unicode(str_pitem, 'utf-8'))
            self.rank_file.write(u"</td>")
        self.rank_file.write(u'</tr>')

    #写入结尾备注
    def write_note(self):
        self.rank_file.write(u'''
<div align="center" style="margin: auto;max-width: 800px">
    <p align="left">
        ''')
        self.rank_file.write(setting.Note)
        self.rank_file.write(u'''</p></div>
        </div><div style="align: center" id="footer">
        <p align="center">Posted by: 雪靡 | <a href="https://github.com/736248591/hduReader">Source on GitHub </a></p>
    </div>
</body>
''')
    # 结束使用
    def end(self):
        self.rank_file.write(u'</table>')
        self.write_note()
        self.rank_file.write(u'</html>')
        self.rank_file.close()
        del self.rank_file
        # 生成最终文件
        shutil.move(TEMP_FILE_NAME, FILE_NAME)
