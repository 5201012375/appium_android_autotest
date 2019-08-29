#coding=utf
from business.mine_business import *
import unittest
import HTMLTestRunner
class MineProject(unittest.TestCase):
    # def __init__(self):
    #     pass
    def test_login(self):
        m = MineProjectBusiness()
        username = m.login_business()
        self.assertEqual("纳格纳罗斯", username)


#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)