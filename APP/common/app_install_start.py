import os
import time
import subprocess
import multiprocessing
from time import ctime
from appium import webdriver
class InstallStart(object):
    def __init__(self,host,port,deviceindex):
        self.host = host
        self.port = port
        self.deviceindex = deviceindex
        self.deviceport = str(21503 + 10 * self.deviceindex)
    def preparework(self):
        """连接模拟器方法"""
        print(11111111111)
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
        #在此次添加测试方法
        ####################################
        return self.driver
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
    def appium_server(self):
        """启动appium服务"""
        print(258258258)
        bport = self.port + 2 * self.deviceindex
        cmd = "start /b appium -a" + " " + self.host + " " + "-p" + " " + str(bport) + " " + "-bp" + " " + str(bport + 1)+ " "+ "-U" +" "+ "127.0.0.1:" + self.deviceport

        print(cmd)
        subprocess.Popen(cmd, shell=True, stdout=open("../report/" + str(self.port) + ".log", "w"),
                         stderr=subprocess.STDOUT)
        print(77777777777777777)
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
        """在此设置测试顺序"""
        I = InstallStart(host, port, devicesnum)
        print(22222222)
        I.check_client()
        print(444444)
        I.appium_server()
        print(555555555555555555)
        I.preparework()
    @classmethod
    def mulStart(cls,devicesnum):
        """以多进程方式启动测试"""
        host = "127.0.0.1"
        port = 4723
        pool = multiprocessing.Pool()
        processlist = []
        for deviceindex in range(devicesnum):
            # p = multiprocessing.Process(pool.apply_async(UserLogin.final_start_app,(host,port,deviceindex)))
            # p = multiprocessing.Process(pool.apply_async()
            processlist.append(pool.apply_async(InstallStart.final_start_app,(host, port, deviceindex)))
        pool.close()
        pool.join()
        return processlist
if __name__ == '__main__':
    devicesnum = 2
    f = InstallStart.mulStart(devicesnum)