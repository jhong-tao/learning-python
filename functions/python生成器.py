#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python生成器.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
# 类别推导式，将列表推导式的中括号换成小括号即可
l = (i for i in range(1, 100*100000) if i % 2 == 0)
print(l)

def test():
    print("xxx")
    res1 = yield 1          # send()方法，当在第二次调用生成器的时候可以给res1传递一个参数
    print(res1)
    res2 = yield 2
    print(res2)


# 创建生成器
g = test()

print(g.__next__())         # next()函数不能给上一次挂起的yield 传递参数
# print(g.__next__())
print(g.send("ooo"))        # send()函数可以给yield 在上一次挂起的语句传递参数，send()函数传参的前提是函数体内必须要先有一个yield语句才能传递参数 如果是第一次调用则只能传递一个空值