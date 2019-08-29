#coding=utf-8
import json
import os
class MineData(object):
    def __init__(self):
        """读取json文件"""
        uperdir = os.path.abspath(__file__)
        splitdir = os.path.split(uperdir)
        print(splitdir)
        minedir = os.path.join(splitdir[0],"mine.json")
        with open(minedir,"r") as file:
            self.filedata = json.load(file)
        print(self.filedata)
    def click_mine_xpath(self):
        """app主页我的选项"""
        click_mine_xpath = self.filedata["logincontainer"]["click_mine_xpath"]
        print(click_mine_xpath)
        return click_mine_xpath
    def click_register_longin_id(self):
        """注册登陆选项"""
        click_register_longin_id = self.filedata["logincontainer"]["click_register_longin_id"]
        return click_register_longin_id
    def click_loginbutton_id(self):
        """登陆按钮"""
        click_loginbutton_id = self.filedata["logincontainer"]["click_loginbutton_id"]
        return click_loginbutton_id
    def click_userimag_id(self):
        """用户头像图片"""
        click_userimag_id = self.filedata["logincontainer"]["click_userimag_id"]
        return click_userimag_id
    def send_phoneno_id(self):
        """输入电话号码框"""
        send_phoneno_id = self.filedata["logincontainer"]["send_phoneno_id"]
        return send_phoneno_id
    def send_password_id(self):
        """输入密码框"""
        send_password_id = self.filedata["logincontainer"]["send_password_id"]
        return send_password_id

    def get_personaldata_elem(self):
        """个人资料"""
        get_personaldata_elem = self.filedata["logincontainer"]["get_personaldata_elem"]
        return get_personaldata_elem
    def click_return_id(self):
        """点击个人资料返回键"""
        click_return_id = self.filedata["logincontainer"]["click_return_id"]
        return click_return_id
    def get_mytitle_element(self):
        """获取个人资料全部元素"""
        get_mytitle_element = self.filedata["logincontainer"]["get_mytitle_element"]
        return get_mytitle_element
    def click_save_id(self):
        click_save_id = self.filedata["logincontainer"]["click_save_id"]
        return click_save_id
if __name__ == '__main__':
    print(MineData().get_personaldata_elem())