#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DailyCode 
@File    ：01流程控制之for循环.py
@IDE     ：PyCharm 
@Author  ：wangyuqi
@Date    ：2021/7/15 9:39 下午 
'''
"""
for 循环语法 
for 变量名 in 可迭代对象是： 列表、字典、字符串、元组、集合
    代码1
    代码2
    代码3
    ·····
·····
"""
# 循环取值


# 简单版本
l = ["列表1", "列表2", "列表3"]
for x in l:
    print(x)

# 复杂版本：列表
l1 = ["列表3", "列表4", "列表5"]
i = 0
while i < 3:
    print(l1[i])
    i+=1

# 复杂版本：字典
dic = {'k1':111,'k2':222,'k3':333}
for x in dic:
    print(x,dic[x])