#使用lxml解析标签文本
#lxml能自动补全闭合标签

#豆瓣排行榜网页数据

from requests_html import HTMLSession
from lxml import etree
from openpyxl import workbook
session = HTMLSession()

class DBSpider(object):
    def __init__(self):
        self.start_url = 'https://movie.douban.com/top250'
        self.headers = {
            'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        }
        #创建excel对象
        self.wb = workbook.Workbook()
        #获取当前正在操作的表的对象
        self.ws = self.wb.active
        #设置表头
        self.ws.append(['电影的名称','经典台词'])





    def parse_start_url(self):
        for page in range(5):
            print(f"正在采集第{page}页\n\n\n")
            url = self.start_url.format(page*25)

            response = session.get(url, headers=self.headers)
            self.parse_response_data(response, page)

            """当此时的for循环执行完毕。翻页的请求发送完毕，数据采集完毕"""
            self.wb.save('豆瓣电影信息.xlsx')

    def parse_response_data(self, response, page):

        #解析响应
        html = etree.HTML(response.content.decode('utf-8'))
        #提取电影的li标签对象
        li_list = html.xpath('//ol[@class="grid_view"]/li')
        #遍历电影li标签对象
        for li in li_list:
            #提取电影的标题
            title = ''.join(li.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0])
            #提取电影的经典台词
            text = ''.join(li.xpath('./div/div[2]/div[2]/p[2]/span/text()')[0])

            self.ws.append([title, text])
            print(f'电影{title}数据采集成功')





if __name__ == '__main__':
    db = DBSpider()
    db.parse_start_url()
























