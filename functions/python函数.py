#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python函数.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
# 不定长参数的函数
# 原始方法 给函数的参数传递列表或者元组
def my_sum(tuple):
    print(type(tuple))
    result = 0
    for v in tuple:
        result += v
    print(result)

# 调用
my_sum((1, 2, 3))
# 这种方式，是可以实现一次给函数传递多个变长的参数，把参数放到元组或者列表里，函数体内通过对列表或元组的访问，来实现变长参数的访问

# 第二种方法，在函数参数的前面添加一个*，此时函数会自动将传递的多个参数当做一个元组
def my_sum1(* args):
    print(args, type(args))
    result = 0
    for v in args:
        result += v
    print(result)

# 调用,这一种方式，在调用函数时，传参就可以不以元组的方式传递参数，而是可以将参数，单独一个一个的传递到函数的参数列表
my_sum1(1, 2, 3)

# 第三种方法，在函数参数的前面添加**，此时函数会把穿的的参数当做一个字典
def my_sum3(** kwargs):
    print(kwargs, type(kwargs))
    print(kwargs.keys())

# 调用
my_sum3(name="zs", age=20)


# 拆包操作，当需要把一个集合中的元素分成单独的元素传递个函数作为参数时
def my_sum4(a, b, c):
    print(a + b + c)

def test4(* args):
    print(args)
    print(*args)        # *集合名称  这种方式为拆包方式即用一个*进行拆包
    my_sum4(* args)     # 将参数args拆包后直接传递给my_sum4()，此时拆包后的值与my_sum4()的函数参数一一对应
# 调用
test4(1, 2, 3)

# 字典的拆包方式
def my_sum5(a, b):
    print(a+b)

def test5(**kwargs):
    print(kwargs,type(kwargs))
    # 字典拆包，使用**
    my_sum5(**kwargs)
# 调用
test5(a=1, b=2)
# test5(a=1, c=2)  # 这种方式会报错，需要注意的是装包和拆包后的机构是一模一样的，所以my_sum5()中定义的形参是a和b，所以在传参时必须是一致的

# 参数默认值:默认参数需要放到函数参数列表的尾部

# 函数传参方式：python中函数传参方式只有地址传递，值能不能改变，是根据被传递的数据的类型来决定，可变类型则可以通过函数体改变，不可变类型，则不能改变

# 函数的使用描述

def caculate(a, b=1):
    """
    计算两个数的和，以及差
    :param a: 数值1，数值类型，不可选，没有默认值
    :param b: 数值2，数值类型，可选，默认值为1
    :return: 返回的是计算的结果，元组类型，例：（和，差）
    """
    he = a + b
    cha = a - b
    return (he, cha)

# 直接在函数中声明参考的参数类型和返回值类型
# 参数类型在参数后面加：加类型，表明参数的类型
# 在函数名的（）后面用->加返回值而类型，表名函数值的返回值类型

def caculate1(a:int, b:int=1)->tuple:
    """
    计算两个数的和，以及差
    :param a: 数值1，数值类型，不可选，没有默认值
    :param b: 数值2，数值类型，可选，默认值为1
    :return: 返回的是计算的结果，元组类型，例：（和，差）
    """
    he = a + b
    cha = a - b
    return (he, cha)


help(caculate1)

# 高阶函数
"""
当一个函数在参数中接收另一个函数时，这个函数就被称为高阶函数，被作为参数传递的函数会被高阶函数在函数体中去使用
这个时候高阶函数就可以比较灵活，动态的去实现一些功能
"""
l = [{"name": "zs2", "age":18}, {"name": "zs1", "age": 19}, {"name": "zs", "age3": 20}]

def get_key(l):
    return l["name"]

result = sorted(l, key=get_key)
print(result)

print(get_key({"name": "zs2", "age":18}))

# 动态计算两个数的和与差
def caculat(num1, num2, function):
    result = function(num1, num2)
    print(result)

def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1-num2

caculat(1, 2, sum)
caculat(1, 2, sub)


# 返回函数
"""
根据不同的参数，返回不同的函数
"""
def get_function(flag):
    # 1.定义内部函数
    def sum(a, b):
        return a+b
    def sub(a, b):
        return a-b
    if flag == "+":
        return sum
    elif flag == "-":
        return sub

res = get_function("+")
print(res(1, 2))


# 匿名函数
"""
匿名函数，冒号前的变量为函数参数，冒号后面的表达式为函数体，表达式的计算结果为函数的返回值
"""
res = (lambda a, b: a + b )(22, 2)
print(res)

new_function = lambda a, b: a-b

res = new_function(33, 4)
print(res)

# lambda函数实现排序函数的key
l = [{"name": "zs2", "age":18}, {"name": "zs1", "age": 19}, {"name": "zs", "age3": 20}]

result = sorted(l, key=lambda x: x["name"])
print(result)

# 闭包
"""
闭包就是在函数体内的内部函数调用了外部函数的变量或者参数，并且外部函数将内部函数作为函数的返回值返回，也就是说外部函数返回了内部函数
"""

def test():         # test被称为外部函数
    a = 10          # 外部函数的变量
    def test2():    # test2被称为内部函数
        print(a)    # 内部函数调用了外部函数的参数
    return test2    # 外部函数将内部函数作为外部函数的返回值直接返回

"""
要在闭包的内部函数中修改外部函数的变量时，需要在闭包的内部函数中对外部函数的变量使用nonlocal关键字定义
nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
"""
def test():
    a = 1
    b = 2
    def test2():
        a = 10          # 直接定义在内部函数里的变量
        nonlocal b          # 在闭包的内部函数用nonlocal 关键字指明b不是函数的内部变量，而是内部函数在引用外部函数的变量
        b = 3           # 可以通过，内部函数对外部函数的变量的修改
    print(a)
    print(b)
    test2()
    print(a)
    print(b)
    return test2

new_f = test()


"""
当闭包的内部函数引用外部函数的变量时，外部函数的变量在闭包之后会有值的变化时，当闭包函数被执行是，引用的外部变量的值是在外部函数中的最终值
函数什么时候才会确定内部变量标识真正的值：回答 当在函数被调用的时候，也就是说函数被定义的时候，函数内部的变量是不知道变量真正的值是什么的，只有
当函数被真正的调用的时候，函数内部的变量标识才会真正的去寻找被调用的时刻它真正指引的值
"""
def test():
    a = 1
    def test2():
        print(a)        # 在闭包的内部函数引用了外部函数的变量
    a =2                # 外部函数的变量在闭包之后它的值还会发生变化，那么当test2这个内部函数里引用的a他的值到底是1，还是2呢？
    return test2        # 显然只有当函数test2被调用的时候，test2中的变量标识a才会去寻找此刻a真正指引的值是多少，在这里因为返回了test2这个函数
                        # 显然当test2被返回时test2并没有被执行，而a的值已经变成了2，所以当test2被执行是，a指引的值应该是2
new_f = test()          # 返回函数test2
new_f()                 # 显然当test2()被调用的时候，a的值已经变成了2，所以此刻test2函数内部的a指引的值是2，打印结果是2

def test():
    funcs = []       # 返回函数列表
    for i in range(1,4):
        def test2():
            print(i)           # 每次打印i
        funcs.append(test2)     # 将每次生成的函数返回，但是由于返回的是函数，函数并没有被执行，所以每次打印的i到底是多少并不知道，只有等函数被调用的时候才去寻找此刻i的值，这里i只相当于一个形参，并不知道具体是多少
    return funcs    # 返回函数列表

funcs = test()
funcs[0]()      # 调用函数test2(),但是很显然此时i的值并不是1，而是3，所以打印结果应该是3
funcs[1]()      # 调用函数test2(),但是很显然此时i的值并不是2，而是3，所以打印结果应该是3
funcs[2]()      # 所以函数的参数只有当函数被调用的时候，才知道它真正的值是多少，定义的时候只是一个标识，没有具体的值