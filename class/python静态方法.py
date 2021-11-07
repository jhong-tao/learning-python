#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python静态方法.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""


class Person:
    # 类的静态方法，使用staticmethod装饰器来装饰类中的一个函数，那么该函数就是一个静态函数，不许要传递第一个默认参数
    @staticmethod
    def static_func():
        print("这是一个静态方法")


Person.static_func()  # 通过类直接调用
one = Person()
one.static_func()  # 通过类的实例来调用


class A(Person):
    pass


A.static_func()  # 通过子类调用
