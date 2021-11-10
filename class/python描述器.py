#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python描述器.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
描述器，就是用来做数据合法性验证的，类似java中的getter和setter方法
描述器必须包含三个方法：__get__ __set__ __delete__
描述器的实现有两种方法
第一种方法：用property装饰器来装饰一个操作私有变量的三个方法,这种方法会在类里面写很多代码 然程序很臃肿，可读性差
第二种方法：在一个类中只写这三个方法，解释器会自动将该类解释为一个描述器，当对实例中的变量进行操作时 解释器会自动将这三种操作转移到描述器对象中去操作
"""


# 直接通过property装饰器实现描述器功能
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 直接用property 实现描述器       __age是实例成员比变量

    # 描述器实现方法一 直接对私有变量进行get set delet 装饰

    @property  # get 方法
    def age(self):
        print("数据有效性验证")
        return self.__age

    @age.setter  # set 方法
    def age(self, age):
        print("输入数据合法性检查:%d" % (age))
        self.__age = age

    @age.deleter  # delete 方法
    def age(self):
        print("属性存在性检查")
        del self.__age


# one = Person("张三", 18)
# print(one.age)  # get方法验证
#
# one.age = 20  # set 方法验证
#
# print(one.age)


# 类描述器方法
# 方法二，单独定义一个描述器类
class Name:
    # def __init__(self, name):
    #     print(type(self))
    #     self.name = name        # name 是实例属性

    def __get__(self, instance, owner):
        # self 是描述器这个类Name的实例的实例属性		在例中指的就是Dog类的中name属性 和dog实例中的name属性他们是不一样的
        # instance 是调用Name这个描述器的类中的实例属性   在此列中指的就是 下面的 dog这个实例
        # owner 是调用Name这个描述器的类		在此列中 指的就是下面的Dog类
        # return instance.name
        print("数据有效性验证")
        print(self)
        print(instance)
        print(owner)
        return self.name

    def __set__(self, instance, value):
        # value 是传递进来的值
        print("数据合法性验证")
        self.name = value

    def __delattr__(self, item):
        pass


class Dog:
    name = Name()


# Dog.name      # 验证在类属性中使用 描述器

dog = Dog()
dog.name = 5        # 验证在 实例属性中 使用 描述器
dog.name

