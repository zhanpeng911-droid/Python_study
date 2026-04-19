"""
案例：演示 线程共享 全局变量

细节：
    1.进程之间数据都是相互隔离的，线程之间 数据是可以共享的
    2.多线程，并发，操作同一数据，有可能引发安全问题，需要用到线程同步来解决
"""

#需求：定义1个全局变量，my_list = [] ，创建两个子进程分别给列表添加元素，从列表中提取元素

import threading,time

my_list = []

#往其中添加函数
def write_data():
    for i in range(1,6):
        my_list.append(i)
        print(f'add:{i}')
    print(f'write:{my_list}')

#从中读取数据
def read_data():
    #为了让效果更明显，加入休眠线程
    time.sleep(3)

    print(f'read_data:{my_list}')




if __name__ == '__main__':
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)

    t1.start()
    t2.start()



















