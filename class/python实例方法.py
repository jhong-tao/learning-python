#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python实例方法.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
类创建实例方法
"""


class Person:
    # 创建实例方法，要求实例方法的第一次参数要传递一个实例，来标识该方法是哪个实例的，类似于java的this
    def eat(self, food):
        print("在吃饭" + food)


p = Person()
p.eat("饺子")
