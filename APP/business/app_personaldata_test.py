#coding=utf-8
from common.app_install_start import InstallStart
import os
import time
import subprocess
import multiprocessing
from time import ctime
from appium import webdriver
class PersonalData(InstallStart):
    def __init__(self,host,port,deviceindex):
        super(PersonalData,self).__init__(host,port,deviceindex)
        self.elements = {"头像","姓名","昵称","性别","地域","我的收获地址",
        "手机号码绑定","微信","新浪","QQ","修改密码"}
    def preparework(self):
        """连接模拟器方法"""
        # deviceport = str(21503+10 * self.deviceindex)
        desired_caps = {
          "platformName": "Android",
          "platformVersion": "5.1.1",
          "deviceName": "127.0.0.1:" + self.deviceport,
          "app" : r"E:\BAOJUN-v2.3.15-debug08151123.apk",
          "appPackage": "com.baojun.newterritory",
          "appActivity": "com.baojun.newterritory.ui.StartAdPageActivity",
           "automationName":"UiAutomator2",
           #"udid" : "127.0.0.1：62025",
            "noReset": True
        }
        print(self.deviceport)
        #adb_cmd = "adb connect  127.0.0.1:" + self.deviceport
        print("adb connect  127.0.0.1:" + self.deviceport)
        os.system("adb connect  127.0.0.1:" + self.deviceport)
        print("*******************************")
        #os.system("appium")
        time.sleep(10)
        print("http://127.0.0.1:" + str(self.port + 2 * self.deviceindex) + "/wd/hub")
        print(789789789789779789)
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
        # 如果需要添加测试功能请在#号内调用测试方法。
        ####################################
        self.testLogin()
        testresult = self.test_mine_personalDataView_002()
        ####################################
        print(testresult)
        print(999999999999)
        return testresult
    def testLogin(self):
        """此方法作用：在打开app后查找页面元素，找到登陆页面元素后，输入账号密码，点击登陆按钮"""
        print(77777)
        # com.baojun.newterritory: id / fixed_bottom_navigation_icon
        #(//android.widget.ImageView[@content-desc="icon"])[5]
        guideclick = self.driver.wait_activity('(//android.widget.ImageView[@content-desc="icon"])[5]',15)
        self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="icon"])[5]').click()
        time.sleep(5)
        self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_name").click()
        time.sleep(5)
        self.driver.wait_activity("com.baojun.newterritory:id/login_phone", 5, 2)
        self.driver.find_element_by_id("com.baojun.newterritory:id/login_phone").send_keys("")
        self.driver.find_element_by_id("com.baojun.newterritory:id/login_password").send_keys("")
        loginele = self.driver.find_element_by_id("com.baojun.newterritory:id/login_next")
        loginele.click()
        time.sleep(3)
        # username = self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_name").text
        # print(username)
        # return username
    def test_mine_personalDataView_002(self):
        print(555555555555555)
        # #点击头像跳转到个人资料页
        head = self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_head").click()
        #获取界面标题元素
        time.sleep(10)
        title_first_check = self.driver.find_element_by_class_name("android.widget.TextView")
        title_first_check = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView")'[1]).text
        print(444444444)
        print(type(title_first_check))
        print(title_first_check)
        #点击返回
        returnpage = self.driver.find_element_by_id("com.baojun.newterritory:id/titlebar_toolbar").click()
        #点击用户名称
        time.sleep(3)
        click_username = self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        #检查界面标题元素
        title_second_check = self.driver.find_element_by_id("com.baojun.newterritory:id/titlebar_title").text
        #检查界面元素
        getalleles = self.driver.find_elements_by_xpath("//*")
        print(type(getalleles))
        #使用集合的特性做结果分析
        setchange = set(getalleles)
        setresult = setchange.intersection(self.elements)
        if setresult == self.elements and title_first_check == title_second_check:
            print(8888888888888888888)
            return True
        return False
        # for item in getalleles:
        #     print(item.text)
    @classmethod
    def resultAnalyse(cls, processlist):
        resultlist = [i.get() for i in processlist]
        # for t in processlist:
        #     print(22222222222222)
        #     print(t.get())
        #     print(555555555555555)
        print(resultlist)
        changepro = set(resultlist)
        print(changepro)
        print(len(changepro))
        print(list(changepro)[0])
        if len(changepro) == 1 and list(changepro)[0] == True:
            return True
        return False
    @classmethod
    def final_start_app(cls, host, port, devicesnum):
        """在此设置测试顺序"""
        I = PersonalData(host, port, devicesnum)
        print(22222222)
        I.check_client()
        print(444444)
        I.appium_server()
        I.preparework()

    @classmethod
    def mulStart(cls, devicesnum):
        """以多进程方式启动测试"""
        host = "127.0.0.1"
        port = 4723
        pool = multiprocessing.Pool()
        processlist = []
        for deviceindex in range(devicesnum):
            # p = multiprocessing.Process(pool.apply_async(UserLogin.final_start_app,(host,port,deviceindex)))
            # p = multiprocessing.Process(pool.apply_async()
            processlist.append(pool.apply_async(PersonalData.final_start_app, (host, port, deviceindex)))
        pool.close()
        pool.join()
        return processlist
if __name__ == '__main__':
    devicesnum = 1
    f = PersonalData.mulStart(devicesnum)
    result = PersonalData.resultAnalyse(f)