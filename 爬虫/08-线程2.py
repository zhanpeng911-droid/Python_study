"""
进程之间，没有资源竞争

线程之间资源竞争
"""

# from threading import Thread
# import time
#
# def func(x):
#
#     x.append(4)
#     print('我是func',x)
#
# def function(x):
#     print('我是function',x)
# x = [1,2,3]
#
# if __name__ == '__main__':
#     Thread(target=func, args=(x,)).start()
#     Thread(target=function, args=(x,)).start()

#使用全局解释器锁，又叫GIL解释器锁来解决资源竞争问题
#用线程队列不会产生资源竞争




