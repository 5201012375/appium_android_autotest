#coding=utf-8
import os
import time
from common.get_mine_info import MineData
from common.app_start import StartApp

class MineProjectBusiness(object):
    def __init__(self):
        host = "127.0.0.1"
        port = 4723
        self.driver = StartApp.final_start_app(host,port)
        print(self.driver)

    def login_business(self):
        """此方法作用：在打开app后查找页面元素，找到页面元素后，输入账号密码，点击登陆按钮"""
        print(type(MineData().click_mine_xpath()))
        guideclick = self.driver.wait_activity(MineData().click_mine_xpath(),10)
        time.sleep(10)
        self.driver.find_element_by_xpath(MineData().click_mine_xpath()).click()
        time.sleep(5)
        self.driver.find_element_by_id(MineData().click_register_longin_id()).click()
        time.sleep(5)
        self.driver.wait_activity(MineData().click_loginbutton_id(), 5)
        print(888888888888888)
        self.driver.find_element_by_id(MineData().send_phoneno_id()).send_keys()
        self.driver.find_element_by_id(MineData().send_password_id()).send_keys()
        self.driver.find_element_by_id(MineData().click_loginbutton_id()).click()
        time.sleep(3)
        username = self.driver.find_element_by_id(MineData().click_register_longin_id()).text
        print(username)
        # time.sleep(2)
        # head = self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_head").click()
        # head = self.driver.find_element_by_id("com.baojun.newterritory:id/me_userinfo_image").click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("退出登录")').click()
        return username
    def test_mine_personalDataView_002(self):
        """此方法个人资料页查看，包括头像、姓名、昵称、性别、地域、我的收货地址、手机号码绑定、微信、新浪、QQ、修改密码"""
        elements = {"头像", "姓名", "昵称", "性别", "地域", "我的收货地址",
                         "手机号码绑定", "微信", "新浪", "QQ", "修改密码"}
        #点击头像跳转到个人资料页
        head = self.driver.find_element_by_id(MineData().click_userimag_id()).click()
        # 获取界面标题元素
        title_first_check = self.driver.find_element_by_class_name("android.widget.TextView")
        title_first_check = self.driver.find_element_by_id(MineData().get_mytitle_element()).text
        print(444444444)
        print(type(title_first_check))
        print(title_first_check)
        # 点击返回
        self.driver.find_element_by_id(MineData().click_save_id()).click()
        # 点击用户名称
        time.sleep(3)
        click_username = self.driver.find_element_by_id(MineData().click_register_longin_id()).click()
        # 检查界面标题元素
        title_second_check = self.driver.find_element_by_id(MineData().get_mytitle_element()).text
        # 检查界面所有元素
        getalleles = self.driver.find_elements_by_xpath("//*")
        getalleles = {i.text for i in getalleles}
        print(type(getalleles))
        print(getalleles)
        # 使用集合的特性做结果分析
        setchange = set(getalleles)
        print(setchange)
        setresult = setchange.intersection(elements)
        print(setresult)
        print(elements)
        if setresult == elements and title_first_check == title_second_check:
            print(8888888888888888888)
            return True
        return False
if __name__ == '__main__':
    m = MineProjectBusiness()
    m.login_business()