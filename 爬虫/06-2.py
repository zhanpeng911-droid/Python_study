#采集小说文本
"""
思路分析：
    1.在飞卢小说首页，检索小说，获取搜索结果
        小说数据都是同步加载
    2.提取搜索结果（小说名称，小说详情地址）
    3.访问小说详情地址，获取小说章节数据（章节名称，章节地址）
    4.对小说章节地址发送请求，获取小说正文
"""
import os
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import quote
from lxml import etree
session = HTMLSession()


class BookSpider(object):
    ospath = os.getcwd() + f"/小说/"
    if not os.path.exists(ospath):
        os.makedirs(ospath)
    def __init__(self):
        self.user_input = input('请输入你想采集的小说名字')
        self.start_url = 'https://b.faloo.com/l_0_{}.html?t=1&k={}'
        self.headers = {
            'cookie' : 'host4chongzhi=b.faloo.com; Hm_lvt_6d308f6626f6d0864b6bb4f348f2b5e5=1772628344; HMACCOUNT=2B4BCA458E7D6285; curr_url=https%3A//b.faloo.com/l/0/1.html%3Ft%3D1%26k%3D%25u4e16%25u754c; Hm_lpvt_6d308f6626f6d0864b6bb4f348f2b5e5=1772628481',
            'referer' : 'https://b.faloo.com/l/0/1.html?t=1&k=%u795E%u5893',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        }

    def parse_start_url(self):
        #将用户的输入，进行url转码
        str1 = quote(self.user_input,encoding='gbk')


        for page in range(1, 2):
            #完善地址的拼接
            url = self.start_url.format(page,str1)
            #发送请求
            response = session.get(url, headers=self.headers)


        self.parse_one_response_data(response,page)

    def parse_one_response_data(self, response,page):

        #解析
        soup = BeautifulSoup(response.content.decode('gbk'), 'lxml')
        #提取小说名称和详情地址
        a_list = soup.select('#BookContent > div > div:nth-child(1) > div.TwoBox02_04 > div:nth-child(1) > div.TwoBox02_08 > h1 > a')
        for a in a_list:
            #提取小说名称
            book_name = a.string
            #提取小说详情地址
            book_url = 'https:'+ a.attrs['href']
            #发送请求，获取响应
            response = session.get(book_url, headers=self.headers)
            self.parse_two_response_data(response,page,book_name)
            break

    def parse_two_response_data(self, response, page , book_name):
        """
        爬虫的第三步：解析响应，数据提取
        :param response: 小说详情页地址的响应对象
        :param page:小说对应所在的页码
        :param book_name:小说名称
        :return:
        """
        soup = BeautifulSoup(response.content.decode('gbk'), 'lxml')
        a_list = soup.select('#mulu > div.DivTable > div > div > a')
        for a in a_list:
            #章节名称
            z_name = a.string
            #章节地址
            z_url = 'https:'+ a.attrs['href']

            response = session.get(z_url, headers=self.headers)
            self.parse_three_response_data(response, page, book_name,z_name)
            break

    def parse_three_response_data(self, response, page , book_name,z_name):
        """
        :param response: 章节详情页响应对象
        :param page:小说所在的页码
        :param book_name:小说名称
        :param z_name:章节名称
        :return:
        """
        with open(self.ospath + book_name + '.txt', 'a+',encoding='utf-8') as f:
            f.write(z_name + '\n\n')
            # print(response.content.decode('gbk'))
            soup = BeautifulSoup(response.content.decode('gbk'), 'lxml')
            p_text_list = soup.find_all(class_="noveContent")[0]
            for p in p_text_list:
                text = p.string
                if text :
                    f.write(text)
                print(f"小说{book_name}------{z_name}--------采集完成")



if __name__ == '__main__':
    bookSpider = BookSpider()
    bookSpider.parse_start_url()
















