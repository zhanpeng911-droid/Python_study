"""
课题：selenium环境搭建

知识点：
    1.selenium的介绍
    2.chromedriver的介绍
    3.PhantomJS的介绍
    4.配置chromedriver和PhantomJS
    5.配置Edgedriver
    6.测试
"""

import time
from selenium import webdriver
# edge
driver = webdriver.Edge()
driver.get("http://www.baidu.com")
time.sleep(10)










