"""
知识点：
    1.线程介绍
    2.线程的使用
    3.线程队列
    4.线程池
"""

#线程：程序执行的最小单位
#线程运行在进程中

#一个进程可以有很多个线程

# from threading import Thread
#
# def index(num):
#     print(f'我是{num}')
#
#
# if __name__ == '__main__':
#     #创建t1子进程
#     t1 = Thread(target=index,args=('t1',))
#     #创建t2线程
#     t2 = Thread(target=index,kwargs={'num':'t2' })
#     #启动线程
#     t1.start()
#     t2.start()

"""
谁是主线程，谁是子线程

主线程是当前的文件运行main

t1，t2是子线程

"""

"""线程队列"""
from threading import Thread
from queue import Queue
import time

class Spider(object):

    def __init__(self):
        self.queue = Queue()

    def parse_put_job(self):
        """
        将任务添加到队列容器中
        :return:
        """

        for day in range(1, 31):
            data = f"第{day}天，我依然爱你"
            self.queue.put(data)
        print('子进程t1执行结束')

    def parse_get_job(self):
        """
        从线程队列容器中，获取任务，执行任务
        :return:
        """
        while True:
        # for i in range(1,31):
            data = self.queue.get()
            print(data)

    def run(self):
        """
        线程关联函数
        :return:
        """
        #创建子线程t1，负责将任务添加到队列中
        t1 = Thread(target=self.parse_put_job)
        #创建子线程t2，从队列容器中，获取任务，执行任务
        t2 = Thread(target=self.parse_get_job)
        #启动线程
        t1.start()
        #将t2设置为守护线程
        t2.daemon =True
        t2.start()

if __name__ == '__main__':
    spider = Spider()
    spider.run()
    time.sleep(0.5)
    print("主线程执行结束") 

"""
守护线程：
    当所有非守护线程执行结束，守护线程才会结束
    （当主线程，其他子线程运行结束，守护线程才会结束）
"""













