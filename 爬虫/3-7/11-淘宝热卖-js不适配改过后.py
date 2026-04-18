"""
淘宝JS逆向爬虫案例

功能：搜索淘宝商品并导出到Excel
原理：通过JS逆向生成淘宝API签名，模拟请求获取商品数据
依赖：requests_html, openpyxl, Node.js

使用方法：
1. 安装依赖：pip install requests_html openpyxl
2. 运行：python taobaoremai.py
3. 输入商品名称
"""

import json
from openpyxl import workbook  # 用于操作Excel文件
from requests_html import HTMLSession  # 发送HTTP请求
import time
import re
import subprocess
from urllib.parse import quote

# 创建会话
session = HTMLSession()

# Node.js路径（用于执行JS生成签名）
NODE_PATH = r"C:\Users\Lenovo\AppData\Roaming\JetBrains\PyCharm2025.1\node\versions\24.14.1\node.exe"


class TBSpider(object):
    """淘宝爬虫类"""

    def __init__(self):
        """初始化爬虫，设置请求参数"""
        # 获取用户输入的搜索关键词
        self.user_input = input("请输入查询的商品: ")

        # 淘宝搜索API地址
        self.url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'

        # 请求头，模拟浏览器
        self.headers = {
            # Cookie：淘宝登录凭证（需要定期更新，否则会失效）
            'cookie': 'thw=cn; t=509ac5a2a4040e867ab98c153cafc670; cna=paE+ISwC8mICAXjr7eWOcUNa; xlly_s=1; 3PcFlag=1774701404171; mtop_partitioned_detect=1; _m_h5_tk=36f2612a6716669a7b12a761f10e55e7_1774782476795; _m_h5_tk_enc=832b2f9a7a215ac1610311d8511df059; _tb_token_=bd3e65b0e858; cookie2=1817690ec0b27d2161ee0e6c3851a129',
            'pragma': 'no-cache',  # 禁用缓存
            'referer': 'https://uland.taobao.com/sem/tbsearch?',  # 请求来源
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'  # 浏览器标识
        }

        # 初始化Excel工作簿
        self.wb = workbook.Workbook()
        self.ws = self.wb.active
        # 添加表头
        self.ws.append(['商品名称', '商品价格'])

    def parse_sign_value(self, time_temp, data_str):
        """
        生成淘宝API签名（核心逆向逻辑）

        原理：sign = MD5(token + 时间戳 + appKey + 请求数据)
        步骤：
        1. 从Cookie中提取token
        2. 拼接待加密字符串
        3. 调用Node.js执行JS生成MD5签名

        参数:
            time_temp: 时间戳
            data_str: 请求数据（JSON字符串）

        返回:
            sign: 加密签名
        """
        # 1. 读取MD5加密JS代码
        with open('2.js', 'r', encoding='utf-8') as f:
            js_demo = f.read()

        # 2. 从Cookie中提取token（用于生成签名）（token的值去找）
        token = re.findall('_m_h5_tk=(.*?)_', self.headers['cookie'])[0]

        # 3. 拼接签名原文：token + 时间戳 + appKey + 请求数据
        str_data = f'{token}&{time_temp}&12574478&{data_str}'

        # 4. 转义特殊字符（防止JS语法错误）
        escaped_str = str_data.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')

        # 5. 构造JS代码并执行
        script = f'''
        {js_demo}
        var result = c("{escaped_str}");
        console.log(result);
        '''

        # 6. 写入临时文件（Node.js需要文件才能执行）
        with open('temp_sign.js', 'w', encoding='utf-8') as f:
            f.write(script)

        # 7. 调用Node.js执行JS，生成签名
        result = subprocess.run([NODE_PATH, 'temp_sign.js'], capture_output=True, text=True)
        sign = result.stdout.strip()
        print(f"签名: {sign}")
        return sign

    def parse_start_url(self):
        """
        构建请求URL并发送请求
        """
        # 1. 获取当前时间戳（毫秒）
        time_temp = str(int(time.time() * 1000))

        # 2. 构造请求参数（包含搜索关键词）
        data = {
            "appId": "43356",
            "params": {
                "device": "HMA-AL00",
                "isBeta": "false",
                "from": "nt_history",
                "brand": "HUAWEI",
                "info": "wifi",
                "q": self.user_input,  # 搜索关键词
                "page": "1",
                "n": 48,  # 每页数量
                "sort": "_coefp",  # 排序方式
                # ... 其他固定参数
            }
        }

        # 3. 将字典转为JSON字符串
        data_str = json.dumps(data)

        # 4. 生成签名
        sign = self.parse_sign_value(time_temp, data_str)

        # 5. 构造完整URL参数
        params = f'?jsv=2.7.2&appKey=12574478&t={time_temp}&sign={sign}&api=mtop.relationrecommend.wirelessrecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&callback=mtopjsonp3&data={quote(data_str)}'

        # 6. 拼接完整URL
        url = self.url + params
        print(f"请求URL: {url[:200]}...")

        # 7. 发送GET请求
        response = session.get(url, headers=self.headers).content.decode()
        print(f"响应: {response[:500]}...")

        # 8. 解析响应数据
        self.parse_response_data(response)

    def parse_response_data(self, response):
        """
        解析响应数据，提取商品信息并保存到Excel

        响应格式：mtopjsonp3({...})
        需要去掉前后缀，解析JSON
        """
        try:
            # 去掉JSONP前后缀：mtopjsonp3(...) -> {...}
            response_data = response[12:-1]

            # 解析JSON
            response_dict = json.loads(response_data)

            # 检查是否成功
            if 'data' in response_dict and 'itemsArray' in response_dict['data']:
                # 提取商品列表
                shop_list = response_dict['data']['itemsArray']

                # 遍历商品，提取名称和价格
                for shop in shop_list:
                    item_name = shop.get('title', '')
                    price = shop.get('price', '')

                    # 写入Excel
                    self.ws.append([item_name, price])
                    print(f"商品: {item_name} - {price}")

                # 保存Excel文件
                self.wb.save(f'{self.user_input}_taobao.xlsx')
                print(f"已保存到 {self.user_input}_taobao.xlsx")
            else:
                print("未找到商品数据")
        except Exception as e:
            print(f"解析失败: {e}")


if __name__ == '__main__':
    # 启动爬虫
    t = TBSpider()
    t.parse_start_url()
