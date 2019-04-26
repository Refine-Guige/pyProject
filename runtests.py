#coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner

from tests import login

if __name__=='__main__':


    suite = unittest.TestSuite()
    suite.addTest(login.loginSuite)
    # 直接启动集合
    runner = unittest.TextTestRunner()
  
    runner.run(suite)
