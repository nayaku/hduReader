# -*- coding:utf-8 -*-

######
#   用户类
######
class User:
    # 类成员定义
    user_name = u""
    nike_name = u""
    moto = u""
    solved_number = 0
    submissions = 0
    ac_rate = 0.0

    # 判断这个用户是否合法
    is_legal = True

    # 初始化
    def __init__(self, user_name):
        self.user_name = user_name
        self.is_legal = True

    def __cmp__(self, other):
        if self.solved_number != other.solved_number:
            return self.solved_number > other.solved_number and -1 or 1
        elif self.ac_rate != other.ac_rate:
            return self.ac_rate > other.ac_rate and -1 or 1
        return 0
