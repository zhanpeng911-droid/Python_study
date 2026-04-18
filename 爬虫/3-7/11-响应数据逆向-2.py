"""
采招网数据采集爬虫

功能：采集采招网（bidcenter.com.cn）的招标/中标信息
原理：
    1. 发送POST请求，获取加密的响应数据
    2. 使用AES解密响应数据
    3. 使用正则表达式提取有效的JSON
    4. 解析JSON提取商品信息，保存到Excel

依赖：
    pip install requests_html openpyxl pycryptodome

使用方法：
    python caizhaospider.py
    输入要搜索的关键词（如：计算机、建筑工程等）
"""

# ==================== 导入模块 ====================
from openpyxl import workbook  # 用于操作Excel文件，保存数据
import requests  # 发送HTTP请求（备用）
from Crypto.Cipher import AES  # AES解密库，用于解密响应数据
from urllib.parse import quote  # URL编码，防止中文乱码
import base64  # Base64解码，AES解密前需要先Base64解码
from requests_html import HTMLSession  # 发送HTTP请求
import json  # JSON解析，处理响应数据
import re  # 正则表达式，提取有效JSON


# ==================== 全局配置 ====================
session = HTMLSession()  # 创建会话对象，复用连接


# ==================== 爬虫类定义 ====================
class CZSpider(object):
    """采招网爬虫类"""

    def __init__(self):
        """初始化爬虫"""
        # 采招网搜索API地址
        self.start_url = 'https://interface.bidcenter.com.cn/search/GetRelatedDataHandler.ashx'

        # 获取用户输入的搜索关键词
        self.user_input = input("请输入你想采集的数据内容：")

        # 请求头，模拟浏览器
        self.headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',  # 请求内容类型
            'origin': 'https://search.bidcenter.com.cn',  # 请求来源
            'referer': 'https://search.bidcenter.com.cn/',  # 来源页面
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'  # 浏览器标识
        }

        # 初始化Excel工作簿
        self.wb = workbook.Workbook()
        self.ws = self.wb.active
        # 添加表头
        self.ws.append(['关键词', '网址', '公司名称'])

    def parse_start_url(self):
        """
        发送POST请求，获取响应数据
        """
        # 构造POST请求参数
        data = {
            'from': '6137',  # 来源标识
            'guid': 'EA87722F-4F13-4E8F-E9A7-E68C2E38D6E4',  # 设备唯一标识
            'page': '1',  # 页码
            'location': '6138',  # 地区标识
            'keywords': quote(self.user_input),  # 搜索关键词（URL编码）
            'mod': '0'  # 模式
        }

        # 发送POST请求
        response = session.post(self.start_url, headers=self.headers, data=data).content.decode('utf-8')

        # 调用解密方法处理响应
        self.parse_aes_response(response)

        # 保存Excel文件
        self.wb.save(f'{self.user_input}.xlsx')
        print(f"已保存到 {self.user_input}.xlsx")

    def parse_aes_response(self, response):
        """
        ==================== 核心：AES解密 ====================

        采招网的响应数据是加密的，需要：
        1. Base64解码
        2. AES-CBC解密

        AES解密参数：
        - key（密钥）: 3zKzyf6eEfuDjAG3
        - vi（偏移量）: fyUANZ0qSNZhhNCV
        - 模式: CBC
        """
        # AES解密密钥和偏移量
        key = '3zKzyf6eEfuDjAG3'
        vi = 'fyUANZ0qSNZhhNCV'

        # 创建AES解密器
        ase = AES.new(key.encode('utf-8'), AES.MODE_CBC, vi.encode('utf-8'))

        # 1. Base64解码 -> 2. AES解密 -> 3. UTF-8解码 -> 4. 去除转义字符
        result = ase.decrypt(base64.b64decode(response)).decode('utf-8').replace('\\', '')

        # ==================== 核心：正则提取有效JSON ====================
        #
        # 问题：解密后的数据可能包含多余的字符，导致JSON解析失败
        # 例如：{"ret":true,...}后面可能跟一些乱码
        #
        # 解决方案：使用正则表达式只提取有效的JSON部分
        #
        # 正则表达式：r'(\{"ret".*\})'
        #   - \{ : 匹配左花括号
        #   - "ret" : 匹配"ret"字符串
        #   - .* : 匹配任意字符（贪婪模式）
        #   - \} : 匹配右花括号
        #
        # 这个正则的意思：从"{"开始，到最后一个"}"结束，中间所有内容
        # 作用：提取完整的JSON字符串，去除后面的乱码
        #
        match = re.search(r'(\{"ret".*\})', result)

        if match:
            # 提取匹配的JSON字符串
            json_str = match.group(1)
            print(f"正则提取成功: {json_str[:100]}...")
            # 传递给下一个方法处理
            self.parse_response_data(json_str)
        else:
            print("未找到有效JSON")

    def parse_response_data(self, response):
        """
        解析JSON数据，提取商品信息
        """
        # 1. 解析JSON字符串为字典
        response_dict = json.loads(response)

        # 2. 提取商品列表
        # 字典结构：response_dict['other2']['tjgysList'] 是一个列表
        data_list = response_dict['other2']['tjgysList']

        print(f"找到 {len(data_list)} 条数据")

        # 3. 遍历每条数据，提取信息
        for item in data_list:
            keyword = item['keyword']  # 关键词
            url = item['url']  # 网址
            company = item['company']  # 公司名称

            # 4. 写入Excel
            self.ws.append([keyword, url, company])

            # 5. 打印到控制台
            print(f"关键词: {keyword} | 网址: {url} | 公司: {company}")


# ==================== 程序入口 ====================
if __name__ == '__main__':
    spider = CZSpider()
    spider.parse_start_url()




















