
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

#需求1：自定义get_list()函数，实现返回一个包含1-5整数的生成器

def get_list():
    #定义一个列表
    my_list = []
    for i in range(1, 6):
        #把获取到的整数添加到列表中
        my_list.append(i)
    return my_list

    # return [i for i in range(1, 6)]  #推导式写法

def get_generator():
    for i in range(1, 6):
        #yield方式，获取生成器对象
        yield i     #把每个i放在生成器中，函数结束后，会返回生成器对象


if __name__ == '__main__':
    list = get_list()
    print(list)
    print(type(list))
    print('-'*20)

    my_g = get_generator()
    print(my_g)


    #获取数据
    for i in my_g:
        print(i)















