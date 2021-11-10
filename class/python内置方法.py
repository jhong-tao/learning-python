#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python内置方法.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # __str__类的格式化打印方法，与java的toString一样,重写这个函数可以实现想要的输出，默认是打实例的类型和地址
        return "这个人的姓名是%s,这个人的年龄是%s" % (self.name, self.age)

    def __call__(self, *args, **kwargs):        # __call__就是当实例被调用的时候要去执行的方法
        print("这是一个人叫%s，并且是一个%s" % (self.name, *args))


one = Person("张三", 18)
print(one)      # 验证__str__ 方法

one("男人")      # 验证__call__方法，该方法使得实例对象可以被调用，在调用的时候传递的参数会直接传递给__call__函数
one("女人")      # 可以实现直接给实例对象传参调用，就跟类对象的构造函数一样