import base64

from pip._internal.network import session
from selenium.webdriver.common.by import By
from selenium import webdriver
from PIL import Image
import time
#edge


class TWSpider(object):
    def __init__(self):
        self.login_url = 'http://www.jianjiaoshuju.com/path/login.htm'
        #创建浏览器驱动对象
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.TX_url = ''

    def parse_login_url(self):
        """
        发起登录请求：输入账号密码，处理验证码
        :return:
        """
        self.driver.get(self.login_url)
        time.sleep(2)
        #标签定位
        self.driver.find_element(By.CLASS_NAME,'phoneNo').send_keys('15767411102')
        self.driver.find_element(By.CLASS_NAME,'pwd').send_keys('luckymay11021102')
        """核心-验证码的获取方式"""
        #第一种 截图获取
        self.driver.save_screenshot('验证码首页.png')
        #获取验证码标签大小
        img_div = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/ul/li[3]/div/span/img')

        # #实例化验证码标签对象
        # location = img_div.location
        # #获取标签大小
        # size = img_div.size
        # #获取验证码上下左右四个点的坐标
        # left = location['x']
        # top = location['y']
        # right = left + size['width']
        # bottom = top + size['height']
        # #打开首页验证码
        # photo = Image.open('验证码首页.png')
        # #在验证码首页图片的基础上再次截图
        # img_obj = photo.crop((left, top, right, bottom))
        # #将截取的区域保存到本地
        # img_obj.save('验证码.png')

        # 方法1：直接截取元素（推荐，最简单）
        img_div = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/ul/li[3]/div/span/img')
        img_div.screenshot('验证码.png')
        """调用第三方解决验证码方法"""
        self.parse_start_url()


    def parse_start_url(self):
        """
        第三方图片验证码识别
        :return:
        """
        hearders = {

        }
        #获取本地验证码，base64加密
        with open('验证码.png', 'rb') as f:
            img_data = f.read()
        base64_data = base64.b64encode(img_data)
        data = {

        }
        response = session.post(self.TX_url, data=data, headers=hearders).json()
        print(response)
        #提取验证码的值
        v_code = response['v_code']
        #自动化输入验证码，点击登录
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/ul/li[3]/div/div/input').send_keys(v_code)
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,'submit-btn').click()
        



if __name__ == '__main__':
    spider = TWSpider()
    spider.parse_login_url()

time.sleep(20)






