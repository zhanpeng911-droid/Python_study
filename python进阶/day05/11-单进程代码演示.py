"""
单进程：
    我们目前写的代码都是单进程的，即：前面的代码没有执行结束，后面的代码就不会被执行

"""

import time

def coding():
    for i in range(10):
        print(f'敲代码...{i}')
        time.sleep(0.2)

def music():
    for i in range(10):
        print(f'听音乐...{i}')
        time.sleep(0.2)


if __name__ == '__main__':
    coding()
    music()



























