"""进程队列"""
from multiprocessing import Process, JoinableQueue as Queue
import time
class Spider(Process):
    def __init__(self):
        self.q = Queue()


    def parse_put_job(self):
        """
        将任务添加到队列容器中
        :return:
        任务：url
        """
        for day in range(1, 51):
            data = f"今天是第{day}"
            #添加数据队列容器
            self.q.put(data)
            #此处阻塞队列
            self.q.join()
            """
            
            """
        print('子进程t1执行结束')

    def parse_get_job(self):
        """
        从队列中获取任务，执行任务
        :return:
        爬虫中任务：从队列容器中获取url地址，发送请求，获取响应
        """
        for day in range(1, 51):
            data =self.q.get()
            print(data)

    def run(self):
        """
        进程关联，关联进程执行对应的函数方法
        :return:
        """
        #t1进程:负责将任务添加到容器中，执行parse_put_job函数方法
        t1 = Process(target=self.parse_put_job)
        #t2进程:负责从队列容器中获取任务执行任务，关联parse_get_job函数方法
        t2 = Process(target=self.parse_get_job)
        t1.start()
        #执行进程
        t2.daemon = True
        t2.start()
        """
        阻塞主进程：只要能够在此处阻塞主进程，即可
        """
        t1.join()
        """
        阻塞的意思
        阻塞主进程，当t1子进程执行结束，该阻塞信号释放，让主进程继续往后执行
        """

if __name__ == '__main__':
    spider = Spider()
    spider.run()
    time.sleep(0.5)
    print(f"主进程执行结束")

"""
守护进程：
当主进程运行结束，守护进程直接结束
我们就可以将t2子进程设置为守护进程，主进程运行结束了，t2子进程也就会结束了 
"""
