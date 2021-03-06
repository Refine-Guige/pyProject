#coding=utf-8
import unittest
from report.HTMLTestRunner import HTMLTestRunner

from tests import login

if __name__=='__main__':


    suite = unittest.TestSuite()
    suite.addTest(login.loginSuite)
    # 直接启动集合
    # runner = unittest.TextTestRunner()
    with open(r'./report/CRMAutoTest.html', 'w',encoding="utf-8") as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)
