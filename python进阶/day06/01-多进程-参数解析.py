"""
案例：演示带参数的 多进程代码

进程涉及到的参数如下：
    target          关联的是 当前进程执行的函数
    name            设置当前进程的名字
    args            以元组的形式，给当前进程关联的函数传参
    kwargs          以字典的形式，给当前进程关联的函数传参

细节：
    1. args 方式传参，实参的个数 和 数据类型，顺序 必须和 进程关联的函数的形参列表 一致.
    2. kwargs 方式传参，实参的个数 和 数据类型 必须和 进程关联的函数的形参列表 一致，顺序无所谓.
"""

import multiprocessing
import time

#1.定义函数，表示：敲代码
def coding(name,num):
    for i in range(10):
        print(f'{name}正在敲第{i}行代码')
        time.sleep(0.2)
#2.定义函数，表示：听音乐
def music(name,count):
    for i in range(10):
        print(f'{name}正在听第{i}首音乐')
        time.sleep(0.2)


if __name__ == '__main__':
    #创建两个进程对象，分别关联：上述的两个函数
    #args方式传参，实参的个数和数据类型，顺序必须和进程关联的形参列表一致
    p1 = multiprocessing.Process(target=coding,name='张三',args=('小明',10))
    #kwargs方式传参，实参的个数和数据类型必须和进程关联的函数的形参列表一致，顺序无所谓
    p2= multiprocessing.Process(target=music,name='李四',kwargs={'count':7,'name':'小红'})
    #打印进程的名字
    print(f'p1:{p1.name},p2:{p2.name}')
    #启动进程
    p1.start()
    p2.start()



















