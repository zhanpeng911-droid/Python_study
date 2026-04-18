"""
多进程：
    可以指定每个进程的任务，多个进程之间可以并发，也可以并行执行

多进程实现步骤：
    1. 导包.
       import multiprocessing
    2. 创建进程对象，关联：要执行的任务 (函数).
       p1 = multiprocessing.Process(target=目标函数名)
    3. 开启进程.
       p1.start()

"""

#需求：一边敲代码，一边听音乐

import time
import multiprocessing

def coding():
    for i in range(10):
        print(f'敲代码...{i}')
        time.sleep(0.2)

def music():
    for i in range(10):
        print(f'听音乐...{i}')
        time.sleep(0.2)


if __name__ == '__main__':
    # coding()
    # music()
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)
    p1.start()
    p2.start()


























