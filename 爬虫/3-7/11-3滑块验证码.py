"""滑块验证码解决方案"""
#豆瓣登录
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class DBSpider(object):
    def __init__(self):
        self.url = 'https://www.douban.com/'
        #edge
        self.driver = webdriver.Edge()

    def parse_login_page(self):
        """
        访问豆瓣首页，解析登录
        :return:
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(1)
        #需要导包,定位iframe
        iframe = WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        #iframe切换
        self.driver.switch_to.frame(iframe)
        #定位密码登录按钮，执行点击
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/ul[1]/li[2]'))).click()
        time.sleep(1)

        #输入账号和密码
        WebDriverWait(self.driver,20,0.5).until(
            EC.presence_of_element_located((By.NAME, 'username'))).send_keys('15767411102')
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'password'))).send_keys('1')
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'btn-account'))).click()

        self.parse_yzm_function()

    def parse_yzm_function(self):
        """
        处理验证码逻辑
        :return:
        """

        #定位滑块验证码所在标签
        img_iframe = WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.ID, 'tcaptcha_iframe_dy')))

        #切换到验证码的iframe
        self.driver.switch_to.frame(img_iframe)
        img_div = WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slideBg"]')))
        time.sleep(1)
        #截取验证码图片
        img_div.screenshot('豆瓣滑块验证码.png')
        """将验证码发给第三方识别"""

    def parse_hk_function(self):
        """
        操作鼠标，滑块补全
        :return:
        """
        #定位滑块所在标签
        hk_div = self.driver.find_element(By.XPATH,'//*[@id="tcOperation"]/div[7]')
        #执行鼠标长按滑块
        action(self.driver).click(hk_div).perform()
        #执行鼠标滑动
        action(self.driver).move_by_offset(xoffset=int(response), yoffset=0).perform()
        time.sleep(0.5)
        #松开鼠标
        action(self.driver).release().perform()

if __name__ == '__main__':
    spider = DBSpider()
    time.sleep(3)
    spider.parse_login_page()
    time.sleep(600)


















