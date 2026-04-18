"""彩票的采集和存储"""
from requests_html import HTMLSession
import pymongo

session = HTMLSession()


class CPSpider(object):
    def __init__(self):
        """删掉响应参数callback"""
        self.url = 'https://jc.zhcw.com/port/client_json.php?transactionType=10001001&lotteryId=1&issueCount=50&startIssue=&endIssue=&startDate=&endDate=&type=0&pageNum=1&pageSize=30&tt=0.06316210089636165&_=1775532748145'
        self.headers = {
            'cookie': 'PHPSESSID=rhm4hi196jvosklndbo81q88f6; Hm_lvt_692bd5f9c07d3ebd0063062fb0d7622f=1775532604; HMACCOUNT=37098C35E43183A9; Hm_lpvt_692bd5f9c07d3ebd0063062fb0d7622f=1775532751; SERVERID=d90be8d89d9bb2f16075c6cf0bb1b917|1775532774|1775532603',
            'host': 'jc.zhcw.com',
            'pragma': 'no-cache',
            'referer': 'https://www.zhcw.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
        }

    def parse_start_url(self):
        """发送请求，获取数据"""
        response = session.get(self.url, headers=self.headers).json()
        num_list = response['data']
        lst = []

        for num in num_list:
            dic = {}
            dic['issue'] = num['issue']
            dic['openTime'] = num['openTime']
            frontWinningNum = num['frontWinningNum']
            backWinningNum = num['backWinningNum']
            dic["result_code"] = (frontWinningNum + "," + backWinningNum).replace(" ", ",")
            lst.append(dic)

        print(lst)

        # 循环结束后再插入数据库
        self.insert_data(lst)

    def connect_mongo(self):
        """连接MongoDB"""
        client = pymongo.MongoClient('localhost', 27017)
        db = client['db2']
        collection = db['code']
        return collection

    def insert_data(self, lst):
        """插入数据到MongoDB"""
        collection = self.connect_mongo()
        collection.insert_many(lst)
        print("数据已插入MongoDB")


if __name__ == '__main__':
    spider = CPSpider()
    spider.parse_start_url()




























