"""
请使用多任务形式完成：一边编程、一边听音乐、一边跟同事聊天。要求如下：

	a.使用多进程完成；

	b.使用多线程完成；

	c.分别观察与对比多进程、多线程的执行效果。
"""
import multiprocessing
#多进程完成

# import multiprocessing,time
#
# def coding():
#
#     for i in range(10):
#         print(f'在敲第{i}行代码')
#         time.sleep(0.2)
#
#
# def music():
#
#     for i in range(10):
#         print(f'在听第{i}首音乐')
#         time.sleep(0.2)
#
#
# def talking():
#
#     for i in range(10):
#         print(f'在聊第{i}件八卦')
#         time.sleep(0.2)
#
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=coding)
#     p2 = multiprocessing.Process(target=music)
#     p3 = multiprocessing.Process(target=talking)
#
#     p1.start()
#     p2.start()
#     p3.start()


#多进程完成

import threading,time

def coding():

    for i in range(10):
        print(f'在敲第{i}行代码')
        time.sleep(0.2)


def music():

    for i in range(10):
        print(f'在听第{i}首音乐')
        time.sleep(0.2)


def talking():

    for i in range(10):
        print(f'在聊第{i}件八卦')
        time.sleep(0.2)


if __name__ == '__main__':
    p1 = threading.Thread(target=coding)
    p2 = threading.Thread(target=music)
    p3 = threading.Thread(target=talking)

    p1.start()
    p2.start()
    p3.start()




