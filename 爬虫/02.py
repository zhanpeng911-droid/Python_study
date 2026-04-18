# import requests
#
# url = 'http://www.baidu.com/'
#
# headers = {
#
#     'Cookie' : 'BAIDUID=892C0DE9D715394DA435556365C1BA83:FG=1; BIDUPSID=892C0DE9D715394DA435556365C1BA83; PSTM=1749009402; BDUSS=dvOXo1SVZnd29SN050YzdGM09GWS1WaH55OEN2bHh-Zn5mU1BsUWJMdFF3cVZvSVFBQUFBJCQAAAAAAAAAAAEAAAA6xK72AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA1fmhQNX5od1; BDUSS_BFESS=dvOXo1SVZnd29SN050YzdGM09GWS1WaH55OEN2bHh-Zn5mU1BsUWJMdFF3cVZvSVFBQUFBJCQAAAAAAAAAAAEAAAA6xK72AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA1fmhQNX5od1; MCITY=-257%3A; BD_UPN=12314753; H_WISE_SIDS=63146_66937_67085_67124_67153_67219_67237_67318_67316_67314_67323_67321_67440_67478_67460_67499_67554_67544_67601_67621_67598_67627_67613_67639_67650_67645_67666_67680_67715_67747_67758; H_PS_PSSID=63146_66937_67085_67124_67153_67219_67237_67318_67316_67314_67323_67321_67440_67478_67460_67499_67515_67554_67544_67601_67621_67598_67627_67613_67639_67650_67645_67666_67680_67715_67747_67758; H_PS_645EC=fb3fdv3imHlPVjDJbWbaH10WvVzVgxiYOIjwkuLyLTS2mO%2B2B0lu%2BHC%2BY0wGmOCJjBK5hNagnD7m; BAIDUID_BFESS=892C0DE9D715394DA435556365C1BA83:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; delPer=0; BD_CK_SAM=1; PSINO=6; BDSVRTM=621; COOKIE_SESSION=0_0_0_1_0_1_1_0_0_1_7_0_0_0_0_0_0_0_1770356051%7C1%230_0_1770356051%7C1',
#     'user-argent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
# }
#
# params = {
#     'ie' : 'utf-8',
#     'wd' : 'baidu'
# }
# response = requests.get(url, headers=headers).content.decode()
# print(response)

"""
课程实战：百度贴吧爬虫
需求：采集百度贴吧的响应，并且保存到本地
思路分析：
https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D&fr=personalize_page
https://tieba.baidu.com/f?kw=%E6%8A%97%E5%8E%8B%E8%83%8C%E9%94%85&fr=frs
https://tieba.baidu.com/f?kw=%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E7%BB%88%E6%9C%AB%E5%9C%B0&fr=frs
kw：检索查询参数，只要修改这个参数的值，即可采集任意贴吧

贴吧更新了没有翻页，但pn还是控制，从0开始，每次累加50


"""
#import requests


# import requests
# from urllib.parse import quote
# str1 = '孙笑川'
# print(quote(str1))

# 缺少这两行导入
import requests
from urllib.parse import quote

class Spider(object):
    """
    爬虫原理第一步：准备数据
    """
    def __init__(self):
        self.start_url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.user_input = input('请输入你想采集的贴吧主题<示例：宝马>')
        self.user_input = '明日方舟终末地'
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        }

    def parse_start_url(self):
        """
        爬虫原理第二步：发送请求获取响应
        :return:
        """
        #for循环模拟翻页
        for page in range(5):
            user_inp = quote(self.user_input)
            response = requests.get(self.start_url.format(user_inp,page*50), headers=self.headers).content.decode()
        self.parse_response_data(response,page)


    def parse_response_data(self,response,page):
        """
        爬虫原理第三步：解析响应，数据提取
        :param response:
        :return:
        """

        #获取状态码
        code = response.status_code
        if code == 200:
            #执行解析
            data = response.content.decode()
            self.parse_sava_data(data, page)

    def parse_save_data(self,data,page):
        """
        爬虫原理的第四步：保存数据
        :param data:
        :return:
        """
        with open(self.user_input + '_'+ str(page) + '.html','w',encoding='utf-8')as f:
            f.write(data)
        print(f'贴吧:{self.user_input}---第{page}----数据采集完成')


if __name__ == '__main__':
    s = Spider()
    s.parse_start_url()






















