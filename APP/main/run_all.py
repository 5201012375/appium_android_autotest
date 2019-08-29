# coding=utf-8
import HTMLTestRunner
import unittest
import os
import sys
import time
from tomorrow import threads
from function.app_mine import *
def add_case(casepath,rule):
    discover = unittest.defaultTestLoader.discover(casepath,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case,report_path,nth=0):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = time.strftime("%Y-%m-%d%H%M%S")
    report_abspath = os.path.join(report_path,"result%s.html" %nth )
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()
if __name__ == '__main__':
    # 用例集合
    now = time.ctime()
    uperdir = os.path.split(os.path.abspath(__file__))
    casepath = os.path.join(uperdir[0], "function")
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(parent_dir)
    print(uperdir)
    print(casepath)
    casepath = os.path.join(parent_dir,"function")
    discover = add_case(casepath=casepath,rule="app*.py")
    # 之前是批量执行，这里改成for循环执行
    print(discover)
    print(88888888)
    for i, j in zip(discover, range(len(list(discover)))):
        run_case(i,report_path="D:\\APP\\report",nth=j)  # 执行用例，生成报告
    print(999999999)