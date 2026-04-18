"""提取豆瓣电视剧名称年份"""

data1 = {
    '0': "喜剧",
    '1': "爱情",
    '2': "悬疑",
    '3': "动画",
    '4': "武侠",
    '5': "古装",
    '6': "家庭",
    '7': "犯罪",
    '8': "科幻",
    '9': "恐怖",
    '10': "历史",
    '11': "战争",
    '12': "动作",
    '13': "冒险",
    '14': "传记",
    '15': "剧情",
    '16': "奇幻",
    '17': "惊悚",
    '18': "灾难",
    '19': "歌舞",
    '20': "音乐",
}

from requests_html import HTMLSession

session = HTMLSession()

import json,jsonpath

class DBSpider(object):
    def __init__(self):
        print(json.dumps(data1,ensure_ascii=False,separators=(',',':')))
        self.user_input = input("请输入需要采集类型的序号")
        self.start_url = 'https://m.douban.com/rexxar/api/v2/tv/recommend'
        self.headers = {
            'Cookie' : 'll="118281"; bid=UFD6I_WHepg; push_noty_num=0; push_doumail_num=0; __utmv=30149280.29380; dbcl2="293804340:AFh8GdMzzJc"; ck=cqJK; __utma=30149280.1257231563.1771854864.1772116392.1772519335.3; __utmc=30149280; __utmz=30149280.1772519335.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; frodotk_db="a2c4fe3e7034e5eee84efabb509eb1ca"; _vwo_uuid_v2=DE34549739B7F7660A28CCC908D01F41E|61493c4564bff002ed91772d04485be1; __utmb=30149280.4.10.1772519335',
            'Origin': 'https://movie.douban.com',
            'Referer': 'https://movie.douban.com/tv/',
            'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'

        }

    def parse_start_url(self):
        for page in range(5):
            #构建请求查询参数
            params = {
                'refresh' : '0',
                'start' : page*20,
                'count' : '20',
                'selected_categories' : '{"类型": "' + data1[self.user_input] +'", "形式": "电视剧"}',
                'uncollect' : 'false',
                'score_range' : '0, 10',
                'tags' : data1[self.user_input],
                'ck' : 'cqJK',
            }

            response = session.get(self.start_url, headers=self.headers, params=params).json()
            # print(response)
            self.parse_response_data(response, page)
            break

    def parse_response_data(self, response,page):

        item_list = response['items']
        title_list = jsonpath.jsonpath(item_list, '$[*].title')
        year_list = jsonpath.jsonpath(item_list, '$..year')


        dict_zip_data = {k:v for k,v in zip(title_list,year_list)}
        print(dict_zip_data)




if __name__ == '__main__':
    d = DBSpider()
    d.parse_start_url()







