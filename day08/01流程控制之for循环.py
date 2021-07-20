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


# 二：总结 for 循环与while循环的异同
# 1 相同之处：都是循环 for循环可以干的事，while循环也可以干。
# 2 不同之处：
#           while循环称为条件循环，循环次数取决于条件何时变为假
#           for循环称之为 "取值循环"，循环次数取决in后包含的值的个数


# 三： for循环控制循环次数 range ()

range(1,9) # 输出 1～8
range(1,9,1) # 每次+1 输出1～9

for x in range(5):
    print("循环",x,"次")