"""淘宝js逆向案例"""
import json
from openpyxl import workbook
from requests_html import  HTMLSession
import os
import time,re,js2py
from urllib.parse import quote
session = HTMLSession()

class TBSpider(object):
    def __init__(self):
        self.user_input = input("请输入查询的商品")
        self.url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'
        self.headers = {
            'cookie' : 'thw=cn; t=509ac5a2a4040e867ab98c153cafc670; cna=paE+ISwC8mICAXjr7eWOcUNa; xlly_s=1; 3PcFlag=1774701404171; mtop_partitioned_detect=1; _m_h5_tk=36f2612a6716669a7b12a761f10e55e7_1774782476795; _m_h5_tk_enc=832b2f9a7a215ac1610311d8511df059; _tb_token_=bd3e65b0e858; cookie2=1817690ec0b27d2161ee0e6c3851a129; tfstk=gfomeNYvfqzjR1Cyx1rXy-8FPjYRGoZ_tfIT6lFwz7P5klLjBR0odfVvCEZxr5crZSSvhxhuQfDskKa9GOXjqXjODITjQGqTbBdpvHHbHlZw9k5ZLQPbCYPwer7K8Xm0bBdp2aBzlIEZHX9Sg77zd7y4QGSwE3ygnly4_lJuaR2C7slabLvuBReN3lPVzzyaQlPZ_lJoU7wab-labLDzNRkfINNnGXnyT5YvZWhGu0y0oWk4gxHx4nzflxPoIAiunxNE32SNb020o0bqdsfzkVkQRmn2jgZxK4rzpxtcqkk4KjF-THSu4YHr6ygW1MUSZc4Z0r6wU7omZmZqMFSntocg8mzlQGHnUSquUDJOR7nuMfo0zpI3WuoL8ouJPIUTmJcZcjXGbXk-pmaSjBfz1qeQ4JHXmgqE3RSPFa7etns_UdnP5Na4F8VphhLnE9MCXhvkEwtzu8wXqLvl5Tz4F8qkELbFmry7hVC..; isg=BGNjUhMTDoLEN8L71rrJyeT28qcNWPeaN9V5VJXAv0I41IP2HSiH6kGCzqRa8k-S',
            'pragma' : 'no-cache',
            'referer' : 'https://uland.taobao.com/sem/tbsearch?bc_fl_src=tbsite_T9W2LtnM&channelSrp=bingSomama&clk1=1fc89313e326a68e5056b5b2697f7fee&commend=all&ie=utf8&initiative_id=tbindexz_20170306&keyword=%E8%AE%A1%E7%AE%97%E6%9C%BA&localImgKey=&msclkid=99ce34314b771e7034875df68ffb627e&page=1&preLoadOrigin=https%3A%2F%2Fwww.taobao.com&q=%E8%AE%A1%E7%AE%97%E6%9C%BA&refpid=mm_2898300158_3078300397_115665800437&search_type=item&sourceId=tb.index&spm=tbpc.pc_sem_alimama%2Fa.search_manual.0&ssid=s5-e&tab=all',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'

        }

        self.wb = workbook.Workbook()
        self.ws = self.wb.active
        self.ws.append('商品名称','商品价格')


    def parse_start_url(self):
        """
        准备工作
        :return:
        """
        #获取当前时间戳
        time_temp = str(int(time.time()*1000))
        data = {"appId":"43356","params":"{\"device\":\"HMA-AL00\",\"isBeta\":\"false\",\"grayHair\":\"false\",\"from\":\"nt_history\",\"brand\":\"HUAWEI\",\"info\":\"wifi\",\"index\":\"4\",\"rainbow\":\"\",\"schemaType\":\"auction\",\"elderHome\":\"false\",\"isEnterSrpSearch\":\"true\",\"newSearch\":\"false\",\"network\":\"wifi\",\"subtype\":\"\",\"hasPreposeFilter\":\"false\",\"prepositionVersion\":\"v2\",\"client_os\":\"Android\",\"gpsEnabled\":\"false\",\"searchDoorFrom\":\"srp\",\"debug_rerankNewOpenCard\":\"false\",\"homePageVersion\":\"v7\",\"searchElderHomeOpen\":\"false\",\"search_action\":\"initiative\",\"sugg\":\"_4_1\",\"sversion\":\"13.6\",\"style\":\"list\",\"ttid\":\"600000@taobao_pc_10.7.0\",\"needTabs\":\"true\",\"areaCode\":\"CN\",\"vm\":\"nw\",\"countryNum\":\"156\",\"m\":\"pc_sem\",\"page\":\"1\",\"n\":48,\"q\":\"" + self.user_input + "\",\"qSource\":\"url\",\"pageSource\":\"tbpc.pc_sem_alimama/a.search_manual.0\",\"tab\":\"all\",\"pageSize\":48,\"totalPage\":100,\"totalResults\":4800,\"sourceS\":\"0\",\"sort\":\"_coefp\",\"bcoffset\":\"\",\"ntoffset\":\"\",\"filterTag\":\"\",\"service\":\"\",\"prop\":\"\",\"loc\":\"\",\"start_price\":null,\"end_price\":null,\"startPrice\":null,\"endPrice\":null,\"itemIds\":null,\"p4pIds\":null,\"categoryp\":\"\",\"myCNA\":\"paE+ISwC8mICAXjr7eWOcUNa\",\"clk1\":\"1fc89313e326a68e5056b5b2697f7fee\",\"refpid\":\"mm_2898300158_3078300397_115665800437\"}"}
        params = f'?jsv=2.7.2&appKey=12574478&t={time_temp}&sign={self.parse_sign_value(time_temp,data)}&api=mtop.relationrecommend.wirelessrecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&callback=mtopjsonp3&data='
        #转码
        quote_str = quote(f"{data}")
        url = self.url + params + quote_str
        response = session.get(url, headers=self.headers).content.decode()
        self.parse_json = json.loads(response)

    def parse_response_data(self, response):
        """
        解析商品数据
        :param response:
        :return:
        """
        response_data = response[12:-1]
        #将字符形式的字典数据，转换成py数据类型的字典
        response_dict = json.loads(response_data)
        #提取商品列表信息
        shop_list = response_dict['data']['itemsArray']
        #遍历商品列表
        for shop in shop_list:
            #提取商品信息
            item_name = shop['title']
            price = shop['price']

            data_list = [item_name, price]
            self.ws.append(data_list)





    def parse_sign_value(self,time_temp,data,):
        """
        解析sign的生成
        r.token + "&" + u + "&" + s + "&" + n.data
        :return:
        """
        #从cookie中提取token值
        token = re.findall('_m_h5_tk=(.*?)_',self.headers['Cookie'])[0]
        #加密之前的字符串拼接
        str_data = token + '&' + time_temp + '&' + '12574478' + '&' + f"{data}"
        #创建js执行环境
        js = js2py.EvalJs()
        with open('2.js', 'r', encoding='utf-8') as f:
            js_demo = f.read()
        #将js代码加载到环境中
        js.execute(js_demo)
        #通过环境调用js函数，传入对应的参数，获取js函数的返回值
        sign = js.h(str_data)
        print(sign)
        return sign

if __name__ == '__main__':
    t = TBSpider()
    t.parse_start_url()