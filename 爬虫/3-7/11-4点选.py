from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import WebDriverWait
from pip._internal.network import session
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import base64



class BZSpider(object):
    def __init__(self):
        self.login_url = 'https://www.bilibili.com/'
        self.driver = webdriver.Edge()
        time.sleep(0.5)
        #最大化窗口
        self.driver.maximize_window()

    def parse_login_url(self):
        self.driver.get(self.login_url)

        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div/span'))).click()
        #输入账号和密码
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/form/div[1]/input'))).send_keys('15767411102')
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/form/div[3]/input'))).send_keys('<PASSWORD>')
        #点击登录按钮
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/div[2]/div[2]'))).click()
        time.sleep(2)

        #截图验证码
        img_div = WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]/img')))

        img_div.screenshot('点选验证码.png')

        self.parse_img_func(img_div)


    def parse_img_func(self, img_div):
        """
        第三方图片验证码识别
        :return:
        """
        hearders = {

        }
        #获取本地验证码，base64加密
        with open('点选验证码.png', 'rb') as f:
            img_data = f.read()
        base64_data = base64.b64encode(img_data).decode()
        data = {

        }
        response = session.post(self.login_url, data=data, headers=hearders).json()
        data = response['data']['data']
        self.parse_login_url(data,img_div)

    def parse_click_img_html(self,data,img_div):
        """
        执行鼠标点选验证码区域坐标
        :param data:
        :return:
        """

        img_div = WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'geetest_item_img')))

        for code_data in data.split('|'):
            x = code_data.split(',')[0]
            y = code_data.split(',')[1]
            #执行点击
            action(self.driver).move_to_element_with_offset(img_div,x,y).perform()
            #每次执行点击之后，模拟人为反应
            time.sleep(0.5)


if __name__ == '__main__':
    spider = BZSpider()
    time.sleep(3)
    spider.parse_login_url()
    time.sleep(30)




