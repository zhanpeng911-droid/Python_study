"""
课程实战：斗鱼直播自动弹幕

需求：对颜值直播间发送表白信息
"""

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
#edge

class DYSpider(object):
    def __init__(self):

        self.start_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Edge()

    def parse_start_url(self):
        """
        访问斗鱼直播间，进行登录
        :return:
        """

        self.driver.get(self.start_url)
        time.sleep(0.5)
        self.driver.maximize_window()
        time.sleep(2)
        # self.driver.find_element(By.XPATH, '//*[@id="js-header"]/div/div[1]/div[4]/div[9]/div/div/a/span').click()
        # time.sleep(30)

        #这里加入防检测


        self.parse_one_url()

    def parse_one_url(self):
        """
        访问所有直播列表页,点击颜值分类
        :return:
        """

        self.driver.find_element(By.XPATH,'//*[@id="js-aside"]/div/div/div/div[1]/div[1]/dl[5]/dd/a[6]').click()
        time.sleep(5)

        self.parse_response_data()


    def parse_response_data(self):
        """
        解析颜值直播间的数量，遍历访问
        :return:
        """

        l_list = self.driver.find_elements(By.XPATH,'//*[@id="listAll"]/div[2]/ul/li')
        #遍历颜值直播间

        room_list = []
        for num in range(1,len(l_list)+1):
            a_href = self.driver.find_element(By.XPATH,'//*[@id="listAll"]/div[2]/ul/li[{}]/div/div/div/a'.format(num)).get_attribute('href')
            #将直播间地址存储到列表中
            room_list.append(a_href)

        #当for循环执行完毕，room_list有所有直播间地址
        self.parse_a_href(room_list)



    def parse_a_href(self, room_list):
        """
        访问直播间，发送弹幕
        :param a_href:
        :return:
        """
        for room_url in room_list:
            js = f'window.open("{room_url}")'
            self.driver.execute_script(js)
            #获取浏览器窗口
            win = self.driver.window_handles
            #切换到直播间窗口
            self.driver.switch_to.window(win[1])
            #定位弹幕输入框
            text = 'zhubo'
            self.driver.find_element(By.XPATH,'').send_keys(text)
            time.sleep(3)
            self.driver.find_element(By.XPATH,'').click()





if __name__ == '__main__':
    spider = DYSpider()
    spider.parse_start_url()



















