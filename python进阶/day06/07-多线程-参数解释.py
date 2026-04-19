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
#需求：使用多进程模拟小明一边编写num行代码，一边听count首音乐功能实现

import threading,time

#定义函数，模拟：写代码
def coding(name,num):
    for i in range(10):
        print(f'{name}正在敲第{i}代码')
        time.sleep(0.1)

#定义函数，模拟：听音乐
def music(name,count):
    for i in range(10):
        print(f'{name}正在听第{i}音乐')
        time.sleep(0.1)

if __name__ == '__main__':
    #创建线程对象
    t1 = threading.Thread(target=coding,name='aaa',args=('小明',10))
    print(f't1线程的名字：{t1.name}')

    t2 = threading.Thread(target=music,name='bbb',kwargs={'name':'ccc','count':10})
    print(f't1线程的名字：{t2.name}')
    #启动线程
    t1.start()
    t2.start()




























