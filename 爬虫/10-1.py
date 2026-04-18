"""
课题：常见标签定位方法与其他方法
"""
from selenium.webdriver.common.devtools.v96.dom import get_attributes

"""1.无头模式，后台运行"""
# from selenium import webdriver
# from selenium.webdriver import EdgeOptions
# import time
# #设置配置的对象
# option = EdgeOptions()
# #第一种
# # option.add_argument('--headless')
# #第二种
# option.headless = True
#
# driver = webdriver.Edge()
# #浏览器窗口最大化
# driver.maximize_window()
# #自定义浏览窗口大小
# driver.set_window_size(1024, 768)
#
# url = 'http://www.baidu.com'
# driver.get(url)
# #获取elements源码内容
# html = driver.page_source
# print(html)
# #时间等待防止浏览器自动退出
# # time.sleep(10)

"""2.加载网页后的常规操作"""
# from selenium import webdriver
# import time
# #edge
# driver = webdriver.Edge()
# url = 'http://www.baidu.com'
# driver.get(url)
#
# driver.maximize_window()
# #获取elements源码内容
# html = driver.page_source
# print(html)
# #关闭当前页面
# driver.close()
# #退出浏览器
# driver.quit()

"""3.webderiver操作浏览器的方式"""
# from selenium import webdriver
# import time
# #edge
# driver = webdriver.Edge()
# url1 = 'http://www.baidu.com'
# driver.get(url1)
# time.sleep(5)
# ##刷新当前网页
# url2 = 'http://www.douban.com'
# driver.get(url2)
# time.sleep(5)
# url3 = 'http://www.bilibili.com'
# driver.get(url3)
# time.sleep(5)
# ##浏览器回退页面
# driver.back()
# time.sleep(2)
# ##浏览器前进页面
# driver.forward()
# time.sleep(5)
# #关闭当前页面
# driver.close()
# #退出浏览器
# driver.quit()

"""4.标签定位方法"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# #edge
# driver = webdriver.Edge()
#
# url = 'https://www.baidu.com'
# driver.get(url)
# time.sleep(5)
# """根据标签的id属性进行定位"""
# driver.find_element(By.ID,'chat-textarea').send_keys('爬虫')

# driver.find_element(By.ID,'chat-submit-button').click()
"""根据标签的class属性进行定位"""
# driver.find_element(By.CLASS_NAME,'').click()
"""根据标签的xpath语法进行定位"""
# driver.find_element(By.XPATH,'//*[@id="chat-submit-button"]').click()
"""根据标签的css语法进行定位"""
# driver.find_element(By.CSS_SELECTOR,'#chat-submit-button').click()
"""根据执行JS代码定位标签"""
# js= 'document.getElementByID("chat-submit-button").click()'
#
# js = 'docunment.getElementByClassName("chat-textarea").click()'
#执行js代码
# driver.execute_script(js)
#
# time.sleep(20)

"""5.webdriver其他常用方法"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
#edge
driver = webdriver.Edge()

url1 = 'http://www.baidu.com'
driver.get(url1)
time.sleep(3)


# text = driver.find_element(By.ID,'chat-submit-button')
# #获取该标签的宽度和高度
# #此方法会应用再验证码的解决方案中
# print(text.size)
# time.sleep(20)

# div = driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[3]')
# #获取标签的文本内容
# print(div.text)
# #获取当前页面的标题
# print(driver.title)
# #获取当前页面的url
# print(driver.current_url)
# #定位某个标签
# text = driver.find_element(By.ID,'chat-submit-button')
# #获取属性值
# print(text.get_attribute(''))

"""6.driver对象常用属性方法"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
#edge
driver = webdriver.Edge()

url = 'http://www.baidu.com'
driver.get(url)
time.sleep(3)
driver.maximize_window()
time.sleep(3)
#当前浏览器页面截图
driver.save_screenshot('baidu.jpg')

"""7.webdriver操作鼠标方法"""


"""8.常用键盘操作"""

"""9.标签对象提取文本内容和属性值"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
#edge
driver = webdriver.Edge()

url = 'http://www.baidu.com'
driver.get(url)
div = driver.find_element(By.XPATH)








