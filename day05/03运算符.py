#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DailyCode 
@File    ：03运算符.py
@IDE     ：PyCharm 
@Author  ：wangyuqi
@Date    ：2021/6/20 2:18 下午 
'''


m = 10
n = 20

m = n


# 解压赋值
salary = [11,22,33,4444,555]
mon0 = salary[0]
mon1 = salary[1]
mon2 = salary[2]
mon3 = salary[3]
mon4 = salary[4]
print(mon0)
print(mon1)
print(mon2)
print(mon3)
print(mon4)

mon0,mon1,mon2,mon3,mon4 = salary
# 必须意一一对应 多一个少一个都不行
print(mon0,mon1,mon2,mon3,mon4)


# 可以不对应的解决办法
salary = [11,22,33,4444,555]
# 取前三个值， # 取后三个值 不能取中间
x,y,z,*_ = salary
print(x,y,z)

# 复习



