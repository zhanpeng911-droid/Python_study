"""
需求：将每个英雄的皮肤图片下载到本地，且进行文件夹分类
"""
import os
from multiprocessing import Process,JoinableQueue as Queue
from requests_html import  HTMLSession

session = HTMLSession()


class LOLSpider(object):
    def __init__(self):
        """
        爬虫原理第一步：准备数据
        """
        #采集所有英雄信息的地址
        self.hero_info_all_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2955353'
        #采集英雄信息的地址
        self.hero_info_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2955353'

        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        }
        self.queue = Queue()

    def parse_start_url(self):
        """
        爬虫原理的第二步：发送请求，获取响应
        :return:
        """
        response = session.get(self.hero_info_all_url, headers=self.headers).json()
        hero_list = response['hero']
        for hero in hero_list:
            hero_id = hero['heroId']
            name = hero['name']
            title = hero['title']
            #称号名称拼接
            name_title = name + '_' + title
            #自动创建英雄对应的文件夹
            os_path = os.getcwd() + f"/{name_title}/"
            # 创建目录
            os.makedirs(os_path, exist_ok=True)
            #拼接英雄的详情数据地址
            info_url= self.hero_info_url.format(hero_id)

            #将数据添加到任务队列中
            data = {'info_url':info_url,'os_path':os_path}
            self.queue.put(data)
            # info_response = session.get(info_url, headers=self.headers).json()
            # self.parse_response_data(info_response,os_path)

        # 等待所有任务完成
        self.queue.join()

    def parse_queue_get(self):
        """
        从队列中获取任务
        :return:
        """
        while True:
            data = self.queue.get()
            info_url = data['info_url']
            os_path = data['os_path']
            info_response = session.get(info_url, headers=self.headers).json()
            self.parse_response_data(info_response,os_path)
            self.queue.task_done()

    def parse_response_data(self,info_response,os_path):
        """
        解析英雄详情信息数据
        :param info_response:英雄详情信息数据
        :param os_path: 保存路径
        :return:
        """
        #提取皮肤列表信息
        hero_data_list = info_response['skins']
        for hero_data in hero_data_list:
            #提取手机版本图片
            loadingImg = hero_data['loadingImg']
            #提取电脑版本图片
            mainImg = hero_data['mainImg']
            #保存皮肤名称
            name = hero_data['name']
            #调用保存
            if loadingImg:
                self.parse_save_data(loadingImg,name,os_path,'手机版')
                # Process(target=self.parse_save_data,args=(loadingImg,name,os_path,'手机版')).start()
            if mainImg:
                # Process(target=self.parse_save_data,args=(loadingImg,name,os_path,'电脑版')).start()
                self.parse_save_data(mainImg,name,os_path,'电脑版')


    def parse_save_data(self,img_url,name,os_path,img_type):
        """
        数据保存
        :param self:
        :param img_url: 图片地址
        :param name: 保存使用的图片名称
        :param os_path: 保存路径
        :param img_type: 图片类型
        :return:
        """
        #过滤敏感字符
        name = name.replace('\\','_').replace('/','_')
        #获取图片的二进制数据
        data = session.get(img_url).content
        #保存到文件夹中
        with open(os_path + name +  img_type + '.jpg','wb') as f:
            f.write(data)
        print(f"英雄:{name}-----{img_type}---保存完成！！！")

    def run(self):
        """
        进程函数关联
        :return:
        """
        #t1将任务添加到任务队列中（获取所有英雄id，创建文件夹，拼接英雄详情数据地址）
        #t1进程是添加
        t1 = Process(target=self.parse_start_url)
        #t2从队列中获取任务，执行任务（获取详情地址，发送请求，解析皮肤图片地址）
        #t2有死循环，需要设置守护进程
        t2 = Process(target=self.parse_queue_get)

        #启动进程
        t1.start()
        #将t2进程设置为守护进程
        t2.daemon=True
        t2.start()
        t1.join()



if __name__ == '__main__':
    l = LOLSpider()
    l.run()

"""
进程:
    任务管理器，通过管理器
    进程相当于一个应用
    不一定，具体还需要看电脑性能
    
优化：通过线程来提高爬虫采集效率

注意点：守护进程不允许有子进程

"""











