"""
课题：selenium其他方法
"""
from selenium.webdriver.chrome import webdriver

#知识点
#1.selenium控制标签页的切换
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import time
# #edge
# driver = webdriver.Edge()
# time.sleep(3)
# url = 'http://www.baidu.com'
# driver.get(url)
# """使用执行js代码打开浏览器自动访问豆瓣"""
# url2 = 'http://www.douban.com'
# js = f'window.open("{url2}")'
# driver.execute_script(js)
#
# """
# 注意点：在未执行窗口的切换，selenium始终默认操作第一个浏览器窗口
# """
# #获取当前浏览器所有窗口
# win = driver.window_handles
# #切换到百度窗口
# driver.switch_to.window(win[0])
# driver.find_element(By.ID, 'chat-textarea').send_keys('hello')
# driver.find_element(By.ID, 'chat-submit-button').click()
#
# time.sleep(5)
# driver.switch_to.window(win[1])
# time.sleep(20)


#2.selenium控制iframe的切换
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import time
# #edge
# driver = webdriver.Edge()
#
# url = 'https://mail.163.com/'
# driver.get(url)
# time.sleep(5)
# #定位iframe标签
# iframe = driver.find_element(By.XPATH,'//*[@id="cnt-box"]')
# #执行切换
# driver.switch_to.frame(iframe)
# #定位账号输入
# #3.selenium获取cookie（自动化登录）
# driver.find_element(By.NAME,'email').send_keys('hhhhhh')
# time.sleep(20)

#4.页面等待
"""
使用场景：
    浏览器访问网页的速度是比代码的执行速度要慢的
"""
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import time
# #edge
# driver = webdriver.Edge()
# driver.implicitly_wait(10)
# driver.get("http://www.csdn.net")
#
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import time
# #edge
# driver = webdriver.Edge()
# #针对性的等待，这样的代码结构，能等待到具体的某个标签，性能更优
# WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,'地图'))).click()


#5.执行js与页面滑动

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
#edge
driver = webdriver.Edge()

url = 'https://www.csdn.net'
driver.get(url)
time.sleep(5)
"""js代码控制浏览器页面滑动"""
#参数说明，0参数位置代表起始滑动位置
#       200滑动距离
# js = 'window.scrollTo(0,200)'
for page in range(5):
    js = 'window.scrollTo({},{})'.format(page*500,800*page)
    driver.execute_script(js)
    time.sleep(5)


#6，使用ip代理

#7.替换ua








