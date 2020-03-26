#coding=utf-8
import os
import time
import subprocess
import multiprocessing
from time import ctime
from appium import webdriver
class UserLogin(object):
    """test_mine_login_001"""
    def __init__(self,host,port,deviceindex):
        self.host = host
        self.port = port
        self.deviceindex = deviceindex
        self.deviceport = str(21503 + 10 * self.deviceindex)
    def preparework(self):
        """连接模拟器方法"""
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
        getname = self.test_mine_login_001()
        logout = self.logout()
        return getname
    def check_client(self):
        """检查端口是否被占用，如果被占用释放端口"""
        print(9999999)
        search_port_cmd = "netstat -ano|findstr %s" % (self.port + 2 * self.deviceindex)
        print(search_port_cmd)
        portinfo = os.popen(search_port_cmd).read()
        print(portinfo)
        print(333333333)
        if str(self.port) and "LISTENING" in portinfo:
            location = portinfo.index("LISTENING")
            start = location + len("LISTENING") + 7
            end = portinfo.index("\n")
            print(start)
            print(end)
            # time.sleep(8000)
            print(portinfo)
            pid = portinfo[start:end]
            closeport_cmd = "taskkill -f -pid %s" % pid
            print(closeport_cmd)
            os.popen(closeport_cmd)
        else:
            print("port %s is available" % self.port)
    def test_mine_login_001(self):
        """此方法作用：在打开app后查找页面元素，找到页面元素后，输入账号密码，点击登陆按钮"""
        print(77777)
        guideclick = self.driver.wait_activity('(//android.widget.ImageView[@content-desc="icon"])[5]', 10)
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
        username = self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_name").text
        print(username)
        # time.sleep(2)
        # head = self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_head").click()
        # head = self.driver.find_element_by_id("com.baojun.newterritory:id/me_userinfo_image").click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("退出登录")').click()
        return username
    def appium_server(self):
        """appium服务"""
        print(258258258)
        bport = self.port + 2 * self.deviceindex
        cmd = "start /b appium -a" + " " + self.host + " " + "-p" + " " + str(bport) + " " + "-bp" + " " + str(bport + 1)+ " "+ "-U" +" "+ "127.0.0.1:" + self.deviceport
        print(cmd)
        subprocess.Popen(cmd, shell=True, stdout=open("D:\\AUTOTEST\\apptest\\app_result_collection\\" + str(self.port) + ".log", "w"),
                         stderr=subprocess.STDOUT)
        print("%s at %s" % (cmd, ctime()))
    def logout(self):
        """点击退出登陆"""
        self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="icon"])[5]').click()
        self.driver.find_element_by_id("com.baojun.newterritory:id/me_home_name").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.baojun.newterritory:id/titlebar_menulayout").click()
        time.sleep(4)
    @classmethod
    def final_start_app(cls,host, port, devicesnum):
        I = UserLogin(host, port, devicesnum)
        I.check_client()
        I.appium_server()
        result = I.preparework()
        return result

    @classmethod
    def mulStart(cls,devicesnum):
        host = "127.0.0.1"
        port = 4723
        pool = multiprocessing.Pool()
        processlist = []
        for deviceindex in range(devicesnum):
            # p = multiprocessing.Process(pool.apply_async(UserLogin.final_start_app,(host,port,deviceindex)))
            # p = multiprocessing.Process(pool.apply_async()
            processlist.append(pool.apply_async(UserLogin.final_start_app,(host,port,deviceindex)))
        pool.close()
        pool.join()
        return processlist
    @classmethod
    def resultAnalyse(cls,processlist):
        resultlist = [i.get() for i in processlist ]
        print(resultlist)
        changepro = set(resultlist)
        print(changepro)
        print(len(changepro))
        print(list(changepro)[0])
        if len(changepro) == 1 and list(changepro)[0] == "纳格纳罗斯":
            return True
        return False
if __name__ == '__main__':
    devicesnum = 2
    f = UserLogin.mulStart(devicesnum)
    result = UserLogin.resultAnalyse(f)
