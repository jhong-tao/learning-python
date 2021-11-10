#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python私有化方法装饰器.py
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
用方法三，也就是用装饰器的方式，则不能显示的调用getter和setter方法了
"""


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("数据有效性验证")
        return self.__name

    @name.setter
    def name(self, name):
        print("数据合法性验证")
        self.__name = name


dog = Person("小花")

print(dog.name)

dog.name = "小黄"     # 虽然类内部使用了setter方法，但是用了装饰器，所以这里对变量的访问可以直接用实例名.变量名的方式来访问，而此时的变量名就是被装饰器装饰的getter setter函数名

print(dog.name)