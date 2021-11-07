#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python类方法.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""


class Person:
    # 实例方法
    def eat(self):
        print(self)
    
    # 创建一个类方法，用装饰器classmethod来装饰一个函数，那么该函数就是一个类函数，需要给该函数的第一个参数传递一个类对象参数
    @classmethod
    def class_func(cls):
        print(cls, "这是一个类方法")


Person.class_func()         # 通过类调用
one = Person()
one.class_func()            # 通过实例调用类方法，通过实例的__class__属性找打该实例继承的类传递给类方法的第一个参数cls


# 衍生类，子类,也就是继承该类的子类
class A(Person):
    pass


A.class_func()      # 子类调用父类的类方法，此时传递给类方法的第一个参数cls指示的就是当前这个子类
