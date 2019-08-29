#coding=utf
from business.mine_business import *
import unittest
import HTMLTestRunner
class MineProject(unittest.TestCase):
    # def __init__(self):
    #     pass
    @classmethod
    def setUpClass(cls):
        global driver
        driver = MineProjectBusiness()
    def test_login(self):
        username = driver.login_business()
        self.assertEqual("纳格纳罗斯", username)
    def test_personalDataView(self):
        boolresult = driver.test_mine_personalDataView_002()
        self.assertEqual(True,boolresult)
# if __name__ == '__main__':
#     unittest.main(verbosity=2)