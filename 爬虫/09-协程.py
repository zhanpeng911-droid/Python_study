"""
知识点：
    1.协程yield
    2.协程greenlet
    3.协程gevent
"""

import time
def index():
    while True:
        print(1)
        print(2)
        '切换到func函数执行'
        yield
        time.sleep(0.5)
        print(3)

def func():
    while True:
        print('a')
        print('b')
        '切换到index函数继续往后执行'
        yield
        time.sleep(0.5)
        print('c')

def run():
    a = index()
    f = func()
    for i in range(5):
        next(a)
        next(f)







