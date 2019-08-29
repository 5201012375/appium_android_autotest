#coding=utf-8
import os
import time
import multiprocessing
#import HTMLTestRunner
import unittest
from apptest.app_public_scripts.app_install_start import InstallStart
from appium import webdriver
import threading

class AppBindTest(InstallStart):
    def __init__(self, host, port, deviceindex,):
        super(AppBindTest, self).__init__(host,port,deviceindex)
    def preparework(self):
        """连接模拟器，并在此执行测试方法"""
        print(99999999999999999999999999)
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "127.0.0.1:" + self.deviceport,
            "app": r"E:\BAOJUN-v2.3.15-debug08151123.apk",
            "appPackage": "com.baojun.newterritory",
            "appActivity": "com.baojun.newterritory.ui.StartAdPageActivity",
            "automationName": "uiautomator2",
            # "udid" : "127.0.0.1：62025",
            'unicodeKeyboard': True,
            "noReset": False
        }
        print(self.deviceport)
        # adb_cmd = "adb connect  127.0.0.1:" + self.deviceport
        print("adb connect  127.0.0.1:" + self.deviceport)
        os.system("adb connect  127.0.0.1:" + self.deviceport)
        print("*******************************")
        # os.system("appium")
        time.sleep(10)
        print("http://127.0.0.1:" + str(self.port + 2 * self.deviceindex) + "/wd/hub")
        print(789789789789779789)
        while True:
            try:
                self.driver = webdriver.Remote("http://127.0.0.1:" + str(self.port + 2 * self.deviceindex) + "/wd/hub",desired_caps)
                self.driver.implicitly_wait(5)
                # self.test_mine_login_017()
                print("pppppppppppppp")
                break
            except Exception as e:
                print("connect failed!,waiting for connect again!")
                print(e)
                time.sleep(5)
                continue
        print("mmmmmmmmmmmmmmmmmmmmmmmmmm")
        print(121315)
        #如果需要添加测试功能请在此处调用测试方法。
        self.test_mine_login_017()
        self.change_Personal_Data()
        return self.driver
    def test_mine_login_017(self):
        """此方法作用：在打开app后查找页面元素，找到页面元素后，输入账号密码，点击登陆按钮"""
        print(77777)
        time.sleep(5)
        guideclick = self.driver.wait_activity('(//android.widget.ImageView[@content-desc="icon"])[5]',10)
        self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="icon"])[5]').click()
        time.sleep(10)
        self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_name").click()
        time.sleep(5)
        self.driver.wait_activity("com.baojun.newterritory:id/login_phone", 20, 2)
        self.driver.find_element_by_id("com.baojun.newterritory:id/login_phone").send_keys("18161240187")
        self.driver.find_element_by_id("com.baojun.newterritory:id/login_password").send_keys("ff757500332")
        loginele = self.driver.find_element_by_id("com.baojun.newterritory:id/login_next")

        loginele.click()
    def change_Personal_Data(self):
        # #点击头像跳转到个人资料页
        head = self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_head").click()
        #点击个人资料的头像选项图片
        # head = self.driver.find_element_by_id("com.baojun.newterritory:id/me_userinfo_image").click()
        # time.sleep(5)
        # # head_portrait = self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_head").click()
        # #选择图片更换头像
        # change_head_portrait = self.driver.find_element_by_id("com.baojun.newterritory:id/iv_media_image").click()
        # time.sleep(3)
        # #输入姓名
        # name = self.driver.find_element_by_id("com.baojun.newterritory:id/me_userinfo_realname").send_keys("fasjgekwsag")
        # #输入昵称
        # nickname = self.driver.find_element_by_id("com.baojun.newterritory:id/me_userinfo_nickname").send_keys("那个大螺丝")
        # #选择性别
        # sex = self.driver.find_element_by_id("com.baojun.newterritory:id/me_userinfo_sixlayout").click()
        # time.sleep(3)
        # sex_choice_man = self.driver.find_element_by_id("com.baojun.newterritory:id/me_sex_man").click()
        #选择地域
        l = []
        t = self.driver.current_context.join(l)
        getalleles = self.driver.find_elements_by_xpath("//*")
        for item in getalleles:
            print(item.text)

        time.sleep(3)
        address = self.driver.find_element_by_id("com.baojun.newterritory:id/me_userinfo_addres").click()

        eleclass = self.driver.find_element_by_class_name("android.widget.TextView")
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("河北省")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("石家庄市")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("长安区")').click()
        #选择我的收货地址
        address = self.driver.find_element_by_id("com.baojun.newterritory:id/me_userinfo_buyaddres").click()
        #增加地址
        add_address = self.driver.find_element_by_id("com.baojun.newterritory:id/mall_eorder_next").click()
        name = self.driver.find_element_by_id("com.baojun.newterritory:id/me_add_shipping_addres_name").send_keys("小明")
        phone_no = self.driver.find_element_by_id("com.baojun.newterritory:id/me_add_shipping_addres_phone").send_keys("185837053325")
        city = self.driver.find_element_by_id("com.baojun.newterritory:id/me_add_shipping_addres_addres").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("内蒙古自治区")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("呼和浩特市")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("新城区")').click()
        location = self.driver.find_element_by_id("com.baojun.newterritory:id/me_add_shipping_addres_content").send_keys("糊涂街1号")
        location_default = self.driver.find_element_by_id("com.baojun.newterritory:id/me_add_shipping_addres_default").click()
        location_default = self.driver.find_element_by_id("com.baojun.newterritory:id/me_add_shipping_addres_next").click()

    @classmethod
    def final_start_app(cls, host, port, devicesnum):
        I = AppBindTest(host, port, devicesnum)
        print(22222222)
        I.check_client()
        print(444444)
        I.appium_server()
        I.preparework()

    @classmethod
    def mulStart(cls, devicesnum):
        host = "127.0.0.1"
        port = 4723
        processlist = []
        for deviceindex in range(devicesnum):
            p = multiprocessing.Process(target=AppBindTest.final_start_app, args=(host, port, deviceindex))
            processlist.append(p)
        for j in processlist:
            j.start()
        for t in processlist:
            t.join()


if __name__ == '__main__':
    devicesnum = 2
    f = AppBindTest.mulStart(devicesnum)