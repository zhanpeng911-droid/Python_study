import os
import requests
from requests_html import HTMLSession

session = HTMLSession()


class IMGSpider(object):
    def __init__(self):
        """
        爬虫原理的第一步：准备数据
        :return:
        """
        self.user_input = input('请输入你想采集的图片<示例：宝马>')
        # 修正URL格式，使用正确的API地址
        self.start_url = 'https://image.baidu.com/search/acjson'
        self.headers = {
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Cookie': 'BAIDUID=892C0DE9D715394DA435556365C1BA83:FG=1; BIDUPSID=892C0DE9D715394DA435556365C1BA83; PSTM=1749009402; BDUSS=dvOXo1SVZnd29SN050YzdGM09GWS1WaH55OEN2bHh-Zn5mU1BsUWJMdFF3cVZvSVFBQUFBJCQAAAAAAAAAAAEAAAA6xK72AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA1fmhQNX5od1; BDUSS_BFESS=dvOXo1SVZnd29SN050YzdGM09GWS1WaH55OEN2bHh-Zn5mU1BsUWJMdFF3cVZvSVFBQUFBJCQAAAAAAAAAAAEAAAA6xK72AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA1fmhQNX5od1; MCITY=-257%3A; BAIDUID_BFESS=892C0DE9D715394DA435556365C1BA83:FG=1; ZFY=rdlCy:AvPZVd:AChD08G:AjBwDs7yV:BJ1MZGiItrF8cA1M:C; BAIDU_WISE_UID=wapp_1771678670594_334; __bid_n=19c80476da83728db3b9de; H_PS_PSSID=63146_67085_67219_67316_67440_67478_67499_67554_67544_67601_67645_67715_67747_67758_67733_67792_67805_67831_67855_67857_67850_67860_67862_67863_67869; BA_HECTOR=24808g0k2l8g0lak2h0h802l8g40071kpran927; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; SEARCH_MARKET_URL=http://wenku.baidu.com/ndlaunch/browse/chat?keyword=%25E7%2599%25BE%25E5%25BA%25A6%25E5%259B%25BE%25E7%2589%2587&fr=launch_ad&utm_source=bdss-WD&utm_medium=cpc&utm_account=SS-bdtg79&e_creative=131468862687&e_keywordid=1270201678747&e_unitid=12966611290&aiPicScene=3&bd_vid=7355767626133358904&reqidFail=0&is_query_reqid=1&verticalCateName=AIPIC; H_WISE_SIDS=67085_67219_67316_67440_67478_67554_67544_67601_67645_67715_67747_67758_67733_67805_67831; ab_sr=1.0.1_MGVmODUzY2M4MmJjN2NlOGNjMWU3MjMxNmEwZmRhOTQyYzExMTU4Njk0NmMzYzE2OTU4ZDgxMzZhN2NlM2VmMjdmN2I0ODhjYTk1M2NkNzAzNDRmYTQ1ZTdiZTA0ZTI5MjNiYTAxMDg0NWNhN2ZkNDY3ZWIxNzliNGE1MzAzYjAzODE2NjMzOWY2ZmU1NTNjNWQ1NzUwYjFjYTdmY2M1YQ==',
            'Host': 'image.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        }

    def parse_start_url(self):
        """
        爬虫原理第二步：发送请求，获取响应
        :return:
        """
        for page in range(1):
            params = {
                'tn': 'resultjson_com',
                'word': self.user_input,
                'queryWord': self.user_input,
                'fp': 'result',
                'ala': '0',
                'applid': '9033758069975086360',
                'pn': page * 30,
                'rn': '30'
            }

            try:
                print(f"正在请求第{page}页...")
                response = session.get(self.start_url, headers=self.headers, params=params)
                print(f"状态码: {response.status_code}")

                if response.status_code == 200:
                    # 解析JSON数据
                    data = response.json()
                    # 调用解析方法
                    self.parse_response_data(data)
                else:
                    print(f"请求失败，状态码: {response.status_code}")

            except Exception as e:
                print(f"请求异常: {e}")

            break

    def parse_response_data(self, response_data):
        """
        爬虫原理第三步：解析响应，数据提取
        :param response_data: 百度图片API返回的JSON数据
        :return:
        """
        if 'data' in response_data:
            data_list = response_data['data']
            print(f"找到 {len(data_list)} 条数据")

            # 打印第一条数据的结构，方便调试
            if data_list:
                print(f"第一条数据结构: {data_list[0]}")

            for i, data in enumerate(data_list):
                if data and isinstance(data, dict):
                    # 尝试多种可能的图片URL字段
                    img_url = None
                    possible_url_fields = ['thumburl', 'middleURL', 'hoverURL', 'objURL']

                    for field in possible_url_fields:
                        if field in data:
                            img_url = data[field]
                            print(f"第{i}条数据 - 找到图片URL: {img_url}")
                            break

                    if img_url:
                        try:
                            # 尝试获取标题
                            title = data.get('titleShow', f'image_{i}')
                            # 尝试获取图片格式
                            img_type = data.get('imageFormat', 'jpg')

                            print(f"处理图片: {title}")
                            os_path = os.getcwd() + f'/{self.user_input}/'
                            if not os.path.exists(os_path):
                                os.makedirs(os_path)

                            # 下载图片
                            img_response = session.get(img_url)
                            if img_response.status_code == 200:
                                img_data = img_response.content
                                self.parse_save_data(img_data, title, img_type, os_path)
                            else:
                                print(f"图片下载失败: {img_url}")

                        except Exception as e:
                            print(f"处理第{i}条数据异常: {e}")
                else:
                    print(f"第{i}条数据为空或不是字典")
        else:
            print("响应数据中没有找到data字段")
            print(f"完整响应: {response_data}")

    def parse_save_data(self, data, title, img_type, os_path):
        """
        爬虫原理的第四步：保存数据
        :param data:需要保存的本地的数据
        :param title:需要保存图片的名称
        :param img_type: 需要保存图片的格式
        :param os_path: 需要保存的图片路径
        :return:
        """
        try:
            # 清理文件名中的特殊字符
            safe_title = ''.join(c for c in title if c.isalnum() or c in '._-')
            file_path = os_path + safe_title + '.' + img_type

            with open(file_path, 'wb') as f:
                f.write(data)
            print(f"图片:{safe_title}------------保存完成！！！！")
        except Exception as e:
            print(f"保存图片异常: {e}")


if __name__ == '__main__':
    print("百度图片爬虫启动...")
    # 安装依赖提示
    try:
        from requests_html import HTMLSession
    except ImportError:
        print("请先安装依赖: pip install requests_html lxml[html_clean]")
        exit()

    i = IMGSpider()
    i.parse_start_url()
    print("爬虫任务完成！")