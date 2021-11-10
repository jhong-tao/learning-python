#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> 01-对象的生命周期.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
类创建方法：__new__
类创建好了之后的初始化方法__init__
类的释放方法,当类被释放就执行__del__
例：
创建一个类，用来记录该类当前有多少个实例
"""


class Person:
    __person_num = 0  # 记录实例个数

    def __init__(self):
        Person.__person_num += 1  # 初始化类的时候加1

    def __del__(self):
        Person.__person_num -= 1

    @classmethod
    def print_instances(cls):
        print(cls.__person_num)


one = Person()      # 创建一个类
one.print_instances()   # 打印父类的实例个数
del one     # 删除一个类
Person.print_instances()        # 打印类的实例的个数