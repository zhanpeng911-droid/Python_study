from base64 import decode
from http.cookiejar import CookieJar

import requests

# import requests
#
# url = 'https://www.baidu.com/'
#
# headers = {
#     'Cookie': 'BAIDUID=892C0DE9D715394DA435556365C1BA83:FG=1; BIDUPSID=892C0DE9D715394DA435556365C1BA83; PSTM=1749009402; BDUSS=dvOXo1SVZnd29SN050YzdGM09GWS1WaH55OEN2bHh-Zn5mU1BsUWJMdFF3cVZvSVFBQUFBJCQAAAAAAAAAAAEAAAA6xK72AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA1fmhQNX5od1; BDUSS_BFESS=dvOXo1SVZnd29SN050YzdGM09GWS1WaH55OEN2bHh-Zn5mU1BsUWJMdFF3cVZvSVFBQUFBJCQAAAAAAAAAAAEAAAA6xK72AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA1fmhQNX5od1; MCITY=-257%3A; H_WISE_SIDS=63146_66937_67085_67124_67153_67219_67237_67318_67316_67314_67323_67321_67440_67478_67460_67499_67554_67544_67601_67621_67598_67627_67613_67639_67650_67645_67666_67680_67715_67747_67758; BAIDUID_BFESS=892C0DE9D715394DA435556365C1BA83:FG=1; PAD_BROWSER=1; SMARTINPUT=%5Bobject%20Object%5D; ZFY=rdlCy:AvPZVd:AChD08G:AjBwDs7yV:BJ1MZGiItrF8cA1M:C; COOKIE_SESSION=44_0_1_2_0_1_1_0_1_1_0_0_0_0_0_0_0_0_1770356095%7C2%230_0_1770356095%7C1; BD_UPN=12314753; BAIDU_WISE_UID=wapp_1771678670594_334; __bid_n=19c80476da83728db3b9de; H_PS_PSSID=63146_67085_67219_67316_67440_67478_67499_67554_67544_67601_67645_67715_67747_67758_67733_67792_67805_67823_67825_67827_67831_67855_67857_67850_67860_67862_67863; BA_HECTOR=2gah0101a4a5208l8404ak0l844h871kpoi0e27',
#
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
# }
#
# response = requests.get(url, headers=headers)
# cookies=requests.utils.dict_from_cookiejar(response.cookies)
# print(cookies)

# url = 'https://www.baidu.com'
#
# response = requests.get(url,timeout=3)
# print(response)

# import requests
# from retrying import retry
#
# @retry(stop_max_attempt_number=3)
# def _parse_url(url):
#     # 前面加_代表私有，这里代表私有方法，其他文件调用此包，此属性不能被调用
#     print("*" * 20)
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
#     response = requests.get(url, headers=headers, timeout=3)
#     # 断言：状态码为200，否则报错
#     assert response.status_code == 200
#     return response.content.decode()
#
# def parse_url(url):
#     try:
#         html_str = _parse_url(url)
#     except Exception as e:
#         print(e)
#         html_str = None
#     return html_str
#
# if __name__ == '__main__':
#     url = 'http://www.baidu.com'
#     # url1 = 'www.baidu.com'
#     # print(parse_url(url1)[:20])  # 字符串切片，取前二十个字符
#     print(parse_url(url))

# import requests
#
# url = 'https://www.douban.com/'
#
# headers = {
#     'Cookie' : 'll="118281"; bid=UFD6I_WHepg; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1771854863%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.8cb4=281d935f63d7a485.1771854863.; _pk_ses.100001.8cb4=1; __utma=30149280.1257231563.1771854864.1771854864.1771854864.1; __utmc=30149280; __utmz=30149280.1771854864.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=30149280.1.10.1771854864',
#     'Referer' : 'https://accounts.douban.com/',
#     'sec-ch-ua' : '"Not:A-Brand";v="99", "Microsoft Edge";v="145", "Chromium";v="145"',
#     'sec-ch-ua-mobile' : '?0',
#     'sec-ch-ua-platform' : '"Windows"',
#     'sec-fetch-dest' : 'script',
#     'sec-fetch-mode' : 'no-cors',
#     'sec-fetch-site' : 'same-site',
#     'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
#
# }
#
# response = requests.get(url, headers=headers)
# print(response.content.decode('utf-8'))

# import requests
# from requests import session
#
# #创建会话保持session对象
# session = requests.session()
#
# url = 'https://accounts.douban.com/j/mobile/login/basic'
# headers = {
#     'Cookie' : 'll="118281"; bid=UFD6I_WHepg; __utma=30149280.1257231563.1771854864.1771854864.1771854864.1; __utmc=30149280; __utmz=30149280.1771854864.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.29380; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2215767411102%22%2C%22code%22:%224001%22}; vtoken=undefined; last_login_way=account; __utmb=30149280.19.10.1771854864; login_start_time=1771856584561',
#     'Origin' : 'https://accounts.douban.com',
#     'Referer' : 'https://accounts.douban.com/passport/login_popup?login_source=anony',
#     'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
# }
#
# data = {
#     'remember' : 'true',
#     'name' : '15767411102',
#     'password' : 'Luckymay11021102'
# }
#
# session.post(url, headers=headers, data=data)
#
# response = session.get('https://www.douban.com',headers=headers)
# print(response.content.decode('utf-8'))

# from requests_html import  HTMLSession
#
# session = HTMLSession()
#
# url = 'https://www.taobao.com'
# response = session.get(url).html
#
# print(response.absolute_links)
# #获取响应中的绝对链接----获取完整地址
# print(response.links)
# #获取响应中的相对链接----（地址可能不完整）
# print(response.base_url)
# #获取基本路径地址
# print(response.base.url)
# #获取网页文本
# print(response.text)
# #获取页面的二进制流
# print(response.raw_html.decode('utf-8'),type(response.raw_html))


# from requests_html import HTMLSession
#
# # 创建session请求对象
# session = HTMLSession()
#
# # 修正URL格式
# url = 'https://www.baidu.com/index.php?tn=68018901_58_oem_dg'
# response = session.get(url)
#
# # 使用XPath获取标题
# title = response.html.xpath('/title/text()')
# print(title)  # 应该输出: ['百度一下，你就知道']


