#coding=utf-8
import os
import time
import multiprocessing
# import HTMLTestRunner
from apptest.app_public_scripts.app_install_start import InstallStart
from appium import webdriver
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
##此脚本作用是获取输入账号，密码按下登录键后，获取信息提示，如”登录成功“，”密码错误“##
##此测试项继承自app_install_start.py脚本的InstallStart类，并通过重写方法，达到简化代码量的目的。
class LoginTest(InstallStart):
    def __init__(self,host,port,deviceindex,toast_message):
        """1.打开app，如果设备上没有，则安装app
           2.toast_message为需要验证的提示信息，这种信息存在时间短，并且不会保存在后端。由main方法传入
           3.设计思路是设置2个线程，即两个方法，test_mine_login_017方法负责模拟输入账号密码，并点击登录，
           4.searchToast方法是在后台并行查找我们需要的toast信息。"""
        super(LoginTest, self).__init__(host, port, deviceindex)
        self.toast_message = toast_message
        print("kkkkkkkkkkkkkkkkk")
    def preparework(self):
        """连接模拟器，并在此执行测试方法"""
        print(99999999999999999999999999)
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "127.0.0.1:" + self.deviceport,
            "app": r"E:\BAOJUN-v2.3.12-debug08150900.apk",
            "appPackage": "com.baojun.newterritory",
            "appActivity": "com.baojun.newterritory.ui.StartAdPageActivity",
            "automationName": "uiautomator2",
            # "udid" : "127.0.0.1：62025",
            "noReset": True
        }
        print(self.deviceport)
        print("adb connect  127.0.0.1:" + self.deviceport)
        os.system("adb connect  127.0.0.1:" + self.deviceport)
        print("http://127.0.0.1:" + str(self.port + 2 * self.deviceindex) + "/wd/hub")
        time.sleep(8)
        print(6666666666666666)
        while True:
            try:
                self.driver = webdriver.Remote("http://127.0.0.1:" + str(self.port + 2 * self.deviceindex) + "/wd/hub",desired_caps)
                self.driver.implicitly_wait(5)
                break
            except Exception as e:
                print("connect failed!,waiting for connect again!")
                print(e)
                time.sleep(5)
                continue
        print("mmmmmmmmmmmmmmmmmmmmmmmmmm")
        print(121315)
        #如果需要添加测试功能请在此处调用测试方法。
        self.sync_gettoast()
        return self.driver
    def test_mine_login_017(self):
        """此方法作用：在打开app后查找页面元素，找到页面元素后，输入账号密码，点击登陆按钮"""
        print(77777)
        guideclick = self.driver.wait_activity('(//android.widget.ImageView[@content-desc="icon"])[5]',10)
        self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="icon"])[5]').click()
        time.sleep(5)
        self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_name").click()
        time.sleep(5)
        self.driver.wait_activity("com.baojun.newterritory:id/login_phone", 20, 2)
        self.driver.find_element_by_id("com.baojun.newterritory:id/login_phone").send_keys("")
        self.driver.find_element_by_id("com.baojun.newterritory:id/login_password").send_keys("")
        loginele = self.driver.find_element_by_id("com.baojun.newterritory:id/login_next")

        loginele.click()


        time.sleep(10)
        print(888)
    def searchToast(self):
        """"此方法作用搜索我们需要的提示信息，找到信息并给出打印"""
        toast_element = (By.XPATH, "//*[contains(@text, " + "'" + self.toast_message + "'" + ")]")
        print("1111111111111111111111111111")

        toast_elements = WebDriverWait(self.driver, 1000, 0.2).until(EC.presence_of_element_located(toast_element))
        # toast_element = WebDriverWait(self.driver,1000,0.2).until(lambda x:x.find_element_by_xpath(toast_element))
        print(toast_elements)
        print("获取" + toast_elements.text + "成功")
    def sync_gettoast(self):
        """此方法作用是设置多线程，当app打开后并发执行 test_mine_login_017和 searchToast方法   """
        p1 = threading.Thread(target=self.test_mine_login_017)
        p2 = threading.Thread(target=self.searchToast)
        p2.setDaemon(True)
        for i in [p1,p2]:
            i.start()

    @classmethod
    def final_start_app(cls, host, port, devicesnum,toast_message):
        I = LoginTest(host, port, devicesnum,toast_message)
        print(22222222)
        I.check_client()
        print(444444)
        I.appium_server()
        I.preparework()

    @classmethod
    def mulStart(cls, devicesnum,toast_message):
        host = "127.0.0.1"
        port = 4723
        processlist = []
        # InstallStart.final_start_app(host,port,0)
        # InstallStart.final_start_app(host,port,1)
        for deviceindex in range(devicesnum):
            p = multiprocessing.Process(target=LoginTest.final_start_app, args=(host, port, deviceindex,toast_message))
            processlist.append(p)
        for j in processlist:
            j.start()
        for t in processlist:
            t.join()
if __name__ == '__main__':
    devicesnum = 2
    toast_message = "登陆成功"
    f = LoginTest.mulStart(devicesnum,toast_message)






