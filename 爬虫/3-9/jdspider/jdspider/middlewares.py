# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from datetime import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
#edge


class SeleniumSpiderMiddleware(object):

    #request 和 spider 位置不能弄反
    def process_request(self, request, spider):
        """
        拦截请求对象
        :param request:拦截下来的请求对象
        :param spider:
        :return:
        """
        #因为该方法：拦截是所有的请求对象
        #在此添加判断
        #获取请求对象的请求地址
        url = request.url
        if 'book.jd.com/booksort.html' in url:
            driver = webdriver.Edge()
            driver.get(url)
            time.sleep(8)
            #获取element内容
            html = driver.page_source
            #由HtmlResponse执行替换将请求对象传递给下载器的过程
            #构造上下文
            content = HtmlResponse(
                url=url,
                request=request,
                body=html,
                encoding='utf-8',

            )
            return content





































