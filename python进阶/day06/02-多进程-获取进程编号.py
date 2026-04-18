"""
案例：演示带参数的 进程的编号

细节：
    1. 1 个进程拥有 1 个唯一的 进程 id，当该进程被关闭的时候，进程 id 也会同步释放。即：进程 id 是可以重复使用的.
    2. 知道了进程 id，就可以锁定到唯一的进程，方便我们管理和维护，以及梳理 子进程 和 父进程之间的关系.
    3. 获取当前进程的 id，有两种方式：
       方式 1：os 模块的 getpid() 函数.
       方式 2：multiprocessing 模块的 pid 属性.
    4. 获取当前进程的 父 id，方式如下：
       os 模块的 getppid() 函数，parent Process，父进程.

"""

import multiprocessing
import time
import os

#1.定义函数，表示：敲代码
def coding(name,num):
    for i in range(10):
        print(f'{name}正在敲第{i}行代码')
        time.sleep(0.2)
        #打印当前进程的pid
        print(f'p1进程的id为：{os.getpid()},{multiprocessing.current_process().pid},它的父进程id为：{os.getppid()}')
#2.定义函数，表示：听音乐
def music(name,count):
    for i in range(10):
        print(f'{name}正在听第{i}首音乐')
        time.sleep(0.2)
        print(f'p1进程的id为：{os.getpid()},{multiprocessing.current_process().pid},它的父进程id为：{os.getppid()}')



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



















