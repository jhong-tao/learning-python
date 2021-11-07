#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python类属性相关.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
给类添加属性
"""


class Money:
    pass


# 方法1，当类已经定义好了，直接通过类名.属性名的方式给类添加新的属性值
Money.count = 1

print(Money.count)      # 访问类属性
print(Money.__dict__)

# 方式二，在创建类的时候，在类的内部给类添加属性


class Person:
    name = "zs"         # 在创建类的时候，给类创建类属性
    age = 18


print(Person.age)       # 访问类的属性
print(Person.__dict__)

peter = Person()        # 通过类实例化一个对象
print(peter.name)       # 通过类实例化的对象访问类的属性


# 对象是通过__class__属性来表示他的父类的
print(peter.__class__)      # 打印Peter对象的父类
peter.__class__ = Money    # 通过__class__修改peter对象的父类
print(peter.__class__)      # 打印Peter对象的父类


# 对象属性的访问和修改顺序。原则就是查询（访问）的时候是就近原则，先找自己在找父类。修改（赋值）和增加只操作自己本身，不会去影响父类，自己没有就创建新的并赋值，自己有就直接修改
peter = Person()
print(peter.age)        # 对象继承了父类的age属性 18
print(peter.__dict__)   # 查看Peter对象的属性集合中包含了那些属性 结果为{}空，也就是说peter自身并没有直接拥有任何属性，都是从父类继承来的
peter.age = 20          # 修改对象的age值 ，此时在Peter对象中没有查询到Peter自己直接的age属性，只有其父类有，而需要给age属性赋值，所以程序会直接给Peter对象创建一个age属性并对其赋值，而不是去修改其父类的age属性
print(peter.__dict__)   # 查看peter对象的直接属性列表，可以发现此时多了一个age属性
print(peter.age)        # 查看对象被修改后的age  20
print(Person.age)       # 验证对象修改从父类继承来的属性的修改会不会影响到父类原来的属性值 age 还是18 显然对象修改从父类继承来的属性值不会影响到父类原来的值
Person.age = 30         # 类名.属性名 修改属性值
print(Person.age)       # 查看修改后的属性值age =30  这充分说明，子类是不能直接修改父类的属性值的