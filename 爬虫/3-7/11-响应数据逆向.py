"""响应数据逆向"""
from openpyxl import workbook  # 用于操作Excel文件
import requests
#采招网
#前端json数据的取值方式
#dict = {"a":123,'aa' : {'a':234}
#python取值方法: data['aa']['a']
#前端取值方法：data.aa.a

from requests_html import  HTMLSession
from urllib.parse import quote
session = HTMLSession()
import json

class CZSpider(object):
    def __init__(self):
        self.start_url = 'https://interface.bidcenter.com.cn/search/GetRelatedDataHandler.ashx'
        self.user_input = input("请输入你想采集的数据内容：")
        self.headers = {
            'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin' : 'https://search.bidcenter.com.cn',
            'referer' : 'https://search.bidcenter.com.cn/',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
        }

        self.aes_url = 'http://tool.chacuo.net/cryptaes'
        self.wb = workbook.Workbook()
        self.ws = self.wb.active
        self.ws.append(['相关信息', '地址', '公司名称'])


    def parse_start_url(self):
        """
        发送请求：获取响应
        :return:
        """
        for page in range(1, 4):
            data = {
                'from': '6137',
                'guid': 'EA87722F-4F13-4E8F-E9A7-E68C2E38D6E4',
                'page': f'{page}',
                'location': '6138',
                'keywords': quote(self.user_input),
                'mod': '0'
            }
            response = session.post(self.start_url, headers=self.headers, data=data).content.decode('utf-8')
            self.parse_aes_response(response)
            """当上面翻页的for循环采集完，代表翻页请求数据采集完毕"""
            self.wb.save(f'采招网.xlsx')


    def parse_aes_response(self, response):
        """
        对接第三方，执行解密
        :return:
        注意点：解密频率不能太高
        """
        data = {
            'data' : response,
            'type' : 'aes',
            'arg' : 'm=cbc_pad=zero_block=128_p=3zKzyf6eEfuDjAG3_i=fyUANZ0qSNZhhNCV_o=0_s=utf-8_t=1'

        }
        headers = {
            'cookie' : 'BAIDU_SSP_lcr=https://cn.bing.com/; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1774856587; HMACCOUNT=37098C35E43183A9; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1774858379; __gads=ID=11cceb64e5f3edbc:T=1774856584:RT=1774858376:S=ALNI_MZ7-JG1jU9ArAgd0z9Zc-ZQF-oNig; __gpi=UID=000012342c3cdeff:T=1774856584:RT=1774858376:S=ALNI_MYP5IAyOWH9tbPxypeDZ50jOu80hA; __eoi=ID=0e639fa038668334:T=1774856584:RT=1774858376:S=AA-AfjaTdyANaDznDaK7FcUANctH',
            'host' : 'tool.chacuo.net',
            'origin' : 'https://tool.chacuo.net',
            'pragma' : 'no-cache',
            'referer' : 'http://tool.chacuo.net/cryptaes',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
        }

        response = session.post(self.aes_url, headers=headers, data=data).json()
    #     print(response)
        self.parse_response_data(response)

    def parse_response_data(self, response):
        """
        数据提取响应内容
        :param response:
        :return:
        """
        data = json.loads(response['data'][0])['other2']['tjgysList']
        for i in data:
            name_keyword = i['keyword']
            url = i['url']
            company_name = i['company']
            data = [name_keyword, url, company_name]
            self.ws.append(data)



if __name__ == '__main__':
    spider = CZSpider()
    spider.parse_start_url()







