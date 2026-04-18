import requests
from urllib.parse import quote
import time
import random


class TiebaSpider(object):
    """百度贴吧爬虫"""

    def __init__(self):
        self.start_url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.user_input = '明日方舟终末地'
        # 添加更完整的请求头，模拟真实浏览器
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            # 这里需要添加你的Cookie（从浏览器复制）
            'Cookie': 'BAIDUID=892C0DE9D715394DA435556365C1BA83:FG=1; BIDUPSID=892C0DE9D715394DA435556365C1BA83; PSTM=1749009402; BDUSS=dvOXo1SVZnd29SN050YzdGM09GWS1WaH55OEN2bHh-Zn5mU1BsUWJMdFF3cVZvSVFBQUFBJCQAAAAAAAAAAAEAAAA6xK72AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA1fmhQNX5od1; BDUSS_BFESS=dvOXo1SVZnd29SN050YzdGM09GWS1WaH55OEN2bHh-Zn5mU1BsUWJMdFF3cVZvSVFBQUFBJCQAAAAAAAAAAAEAAAA6xK72AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA1fmhQNX5od1; MCITY=-257%3A; H_WISE_SIDS=63146_66937_67085_67124_67153_67219_67237_67318_67316_67314_67323_67321_67440_67478_67460_67499_67554_67544_67601_67621_67598_67627_67613_67639_67650_67645_67666_67680_67715_67747_67758; BAIDUID_BFESS=892C0DE9D715394DA435556365C1BA83:FG=1; ZFY=rdlCy:AvPZVd:AChD08G:AjBwDs7yV:BJ1MZGiItrF8cA1M:C; H_PS_PSSID=63146_67085_67219_67316_67440_67478_67499_67554_67544_67601_67645_67715_67747_67758_67733_67792_67805_67823_67825_67827_67831; BA_HECTOR=008lah0h242l258k2la50g0galcla71kpjauv26; TIEBA_NEW_PC=1; STOKEN=4c2d2e78554e9e1c3c191a12e1d4484b3fcc2a5c47f2312cce09f5e5a68289ec; USER_JUMP=-1; BAIDU_WISE_UID=wapp_1771678670594_334; TIEBAUID=08df9b3bf7d2cbda5cf67f4c; Hm_lvt_292b2e1608b0823c1cb6beef7243ef34=1771678979; Hm_lpvt_292b2e1608b0823c1cb6beef7243ef34=1771678979; HMACCOUNT=2B4BCA458E7D6285; SEARCH_MARKET_URL=http%3A//wenku.baidu.com/ndcore/browse/index%3Fpv%3Dhome%26fr%3Dlaunch_ad%26utm_source%3Dbingss-WD%26utm_medium%3Dcpc%26utm_account%3DSS-bingtg07%26msclkid%3D8b3dff55f70c14ab300396cc5959a338%26bfetype%3Dnew; __bid_n=19c80476da83728db3b9de; ab_sr=1.0.1_YWNkZmI4MjAwNjY0ZjBjNDVlNjNlNTI3NmU1OGU4YWJiZTM2MDQ0ZWJmNjUwZTZmYzM5NGQ3OGE2Y2Q5NjI1NDcxZTc1YzY4Y2I3MGZkOTA0YzA1ZGNhNjZkMGVkNjg4NDc0MTQwZTAyNmE3ZGM1ZTdiODIwMjJiZTIyNzY0MGRlMDI1NjgyMWU2NDRlMDNiYjRjMTdkZDgwMTQzYjc1ZDc2MzA5ZDFhYjk1MmIxMGY4NzY5OWFhMzgwODg3ZWM0'
        }

    def parse_start_url(self):
        """发送请求获取响应"""
        for page in range(5):
            print(f'开始采集第{page}页...')
            user_inp = quote(self.user_input)
            url = self.start_url.format(user_inp, page * 50)

            # 添加随机延迟，模拟真实用户行为
            time.sleep(random.uniform(2, 4))

            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                self.parse_response_data(response, page)
            except Exception as e:
                print(f'采集第{page}页失败: {e}')
                # 失败后增加延迟
                time.sleep(5)

    def parse_response_data(self, response, page):
        """解析响应，数据提取"""
        code = response.status_code
        if code == 200:
            # 检查是否被重定向到验证码页面
            if 'verify' in response.url or '验证' in response.text:
                print(f'第{page}页触发了验证码，需要手动处理')
                return

            data = response.content.decode('utf-8', errors='ignore')
            self.parse_save_data(data, page)
        else:
            print(f'第{page}页请求失败，状态码: {code}')

    def parse_save_data(self, data, page):
        """保存数据"""
        filename = f'{self.user_input}_{page}.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f'贴吧:{self.user_input}---第{page}页----数据采集完成')


if __name__ == '__main__':
    print('百度贴吧爬虫启动...')
    print('提示：请确保已在代码中添加了正确的Cookie')
    s = TiebaSpider()
    s.parse_start_url()
    print('爬虫任务完成！')