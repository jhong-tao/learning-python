#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python私有化属性.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
__init__(self,必须的变量列表)构造方法，用来初始化实例的时候需要创建必须的变量的时候使用的
私有变量的作用，主要就是只能在类的内部来访问，目的是为了对数据的验证和过滤，保住数据的合法性
为了保证数据的合法性，所以在修改或者访问数据的时候，需要先验证数据是合法的在对数据进行修改和访问
所以需要getter 和setter方法  目的就是不让直接访问数据，在访问之前进行合法性验证
方法一：直接写getter setter方法，显示调用这两个方法
方法二：property (getter, setter)，把getter 和setter方法传递个property函数，来实现不需要显示地调用getter和setter方法，而是通过实例名.属性名的方式调用
方法三：@property装饰器 装饰“变量名方法”  @变量名方法.setter装饰器装饰setter方法

"""


class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print("数据有效性验证")
        return self.__name

    def set_name(self, name):
        print("数据合法性验证")
        self.__name = name

    name = property(get_name, set_name)     # 传递getter 和setter 方法给 property(),实现直接通过实例名.属性名的方式访问私有变量


dog = Animal("小花")
print(dog.get_name())
print(dog.name)         # 直接通过变量名.属性名的方式访问变量，此时的属性名就是接收这个property函数返回值的变量
dog.set_name("小黄")
print(dog.name)
dog.name = "小白"
print(dog.name)