"""
生成器介绍：
    概述：
        生成器就是用来生成数据的，用一个，生成1个，这样可以节省大量的内存空间.
    大白话解释：
        生成器的推导式写法，非常类似于以前我们用的 列表，集合，字典推导式，只不过换成 小括号而已.
    实现方式：
        1. 推导式写法.
        2. yield关键字.
    如何从生成器中获取到数据
        方法1：next()函数，逐个获取
        方法2：遍历生成器即可
"""

#案例1 回顾之前学的列表推导式
#需求：生成1-5个数字

list1 = [i for i in range(1,6)]
print(list1)
print(type(list1))

set1 = {i for i in range(1,6)}
print(set1)
print(type(set1))
print('-'*20)

#案例2

tuple1 = (i for i in range(1,6))
print(tuple1)               #地址值
print(type(tuple1))         #地址值


#案例3
#自定义生成器
my_generator = (i for i in range(1,6))

#从生成器中获取到元素
#方式1：next()逐个获取
print(next(my_generator))
print(next(my_generator))

for i in my_generator:
    print(i)






