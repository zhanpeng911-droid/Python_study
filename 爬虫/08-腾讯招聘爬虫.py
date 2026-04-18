"""
知识点：线程队列与线程池结合
课程实战：腾讯招聘爬虫

需求采集腾讯招聘岗位信息，print输出

思路分析：
    1.抓包观察岗位数据加载方式
        异步加载


"""

from requests_html import  HTMLSession
from queue import Queue
from multiprocessing.dummy import Pool
import time

session = HTMLSession()

class TXSpider(object):
    def __init__(self):
        self.start_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.headers = {
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        }
        #创建线程队列
        self.queue = Queue()
        #创建线程池对象
        self.pool = Pool(5)
        #定义循环条件
        self.is_running = True
        #创建计数
        self.start_num = 0
        self.end_num = 0
        self.num = 0

    def parse_put_url(self):
        """
        补全地址，将地址添加到任务队列中
        :return:
        """
        for page in range(1, 100):
            #拼接完整的地址
            url = self.start_url.format(page)
            #将地址添加到任务队列中
            self.queue.put(url)
            #计数加+1
            self.start_num += 1

    def parse_start_url(self,url):
        """
        发送请求：获取响应
        :return:
        """
        response = session.get(url, headers=self.headers).json()
        """
        数据提取的验证
        """
        data_json = response['Data']['Posts']
        print(data_json,data_json,'\n\n')
        self.num += 1

    def parse_get_url(self):
        """
        从队列中，获取任务
        :return:
        """
        #从队列中获取任务，执行任务
        url = self.queue.get()
        print(url)
        self.parse_start_url(url)
        #成功采集到一页数据，计数+1
        self.end_num += 1

    def _callback(self,item):
        if self.is_running:
            self.pool.apply_async(self.parse_get_url,callback=self._callback)

    def parse_run(self):
        #调用执行任务添加
        self.parse_put_url()

        #通过队列池回调的方式，来启动从队列中获取任务，执行任务
        for i in range(10):
            self.pool.apply_async(self.parse_get_url,callback=self._callback)

        #防止主线程结束
        while True:
            time.sleep(0.1)
            if self.start_num <= self.end_num:
                self.is_running = False


if __name__ == '__main__':
    spider = TXSpider()
    spider.parse_run()




