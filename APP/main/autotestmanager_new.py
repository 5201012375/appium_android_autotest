#coding=utf-8
import unittest
import HTMLTestRunner
import time
from apptest.app_ui_test.app_userlogin_test import *
class TestManager(unittest.TestCase):
    # def __init__(self):
    #      super().__init__(methodName="runTest")

    def test_mine_login001(self):
        devicesnum = 2
        f = UserLogin.mulStart(devicesnum)
        result = UserLogin.resultAnalyse(f)
        print(result)
        print(77777777777777)
        self.assertEqual(result,True)




if __name__ == '__main__':
    U = unittest.TestSuite()
    U.addTest(TestManager("test_mine_login001"))
    now = time.strftime("%Y-%m-%d%H%M%S")
    # filename = open(os.path.join('D:\\AUTOTEST\\apptest\\app_result_collection\\')+ now + ".html","wb")
    filename = open("D:\\AUTOTEST\\apptest\\app_result_collection\\" + now +"result.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=filename,
        title="单元测试报告",
        description ="单元测试报告",
        )
    runner.run(U)
    filename.close()
    print(88888888888888888)