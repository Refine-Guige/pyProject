#codeing=utf-8

from unittest import TestCase

import requests
import urllib3
import json
import  unittest


#禁用 urllib3
urllib3.disable_warnings()
#需要登陆的接口，需要用session请求；把请求头中的cookie去掉
domaimAddress="https://crm.innertest3.ipaylinks.com"
session = requests.session()

headers = {"Content-Type": "application/json",
           "Accept":"application/json, text/plain, */*",
           "Accept-Encoding":"gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
           "Content-Length": "186",
           "Host": "crm.innertest3.ipaylinks.com",
           "LANG": "zh-CN",
           "Origin": "https://crm.innertest3.ipaylinks.com",
           "Referer": "https://crm.innertest3.ipaylinks.com/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
           "AUTH_TOKEN": "",
           "connect": "keep-alive"}
class A_Login(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress + "/mps-gateway/api/auth/login"
        self.loginAccount = "rufei.wang@ipaylinks.com"
        self.loginDeviceId = "ba279af87be6e1ec8732cf79691e95e9"
        self.loginIp = ""
        self.loginName = "mpsAutoTest"
        self.loginPwd = "refine123"
        self.loginType = ""
        self.verifyCode = "6a204bd89f3c8348afd5c77c717a097a"

        self.test_data = {}

    def test(self):
        self.test_data.update({"loginAccount": self.loginAccount})
        self.test_data.update({"loginDeviceId": self.loginDeviceId})
        self.test_data.update({"loginIp": self.loginIp})
        self.test_data.update({"loginName": self.loginName})
        self.test_data.update({"loginPwd": self.loginPwd})
        self.test_data.update({"loginType": self.loginType})
        self.test_data.update({"verifyCode": self.verifyCode})

        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\n"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['status'], "1")
        self.assertEqual(response['data']['responseCode'], "00000000")
        self.assertEqual(response['data']['responseMsg'], "成功响应")
        self.assertEqual(response['data']['responseStatus'], "1")
        self.assertEqual(response['data']['memberId'], "10000104399")
        self.assertEqual(response['data']['loginName'], "mpsAutoTest")


class B_Homepage_announcement(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress+"/mps-gateway/api/index/announcement"
        self.getNotReadCount = "true"
        self.readStatus = "0"
        self.test_data = {}

    def test(self):
        self.test_data.update({"getNotReadCount": self.getNotReadCount})
        self.test_data.update({"readStatus": self.readStatus})


        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\t"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['message'],"成功")
        self.assertEqual(response['data']['responseCode'],"00000000")
        self.assertEqual(response['data']['responseMsg'], "成功")
        self.assertEqual(response['data']['responseStatus'], "1")



class B_Homepage_myaccount_merchant(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress+"/mps-gateway/api/myaccount/merchant"
        self.test_data = {}

    def test(self):

        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\n"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['message'],"成功响应")
        self.assertEqual(response['status'],"1")


class B_Homepage_myaccount_operator(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress+"/mps-gateway/api/myaccount/operator"
        self.test_data = {}

    def test(self):

        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\n"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['message'],"成功响应")
        self.assertEqual(response['status'],"1")


class B_Homepage_mymenu(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress+"/mps-gateway/api/security/mymenu"
        self.test_data = {}

    def test(self):

        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\n"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['message'],"成功")
        self.assertEqual(response['status'],"1")
        self.assertEqual(response['data']['responseCode'],"00000000")
        self.assertEqual(response['data']['responseMsg'], "成功")
        self.assertEqual(response['data']['responseStatus'], "1")

class B_Homepage_pending_schedule(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress+"/mps-gateway/api/index/pending_schedule"
        self.test_data = {}

    def test(self):

        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\n"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['message'],"首页待办获取成功")
        self.assertEqual(response['status'],"1")


class B_Homepage_menu_quick_entrance(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress+"/mps-gateway/api/index/menu_quick_entrance"
        self.test_data = {}

    def test(self):

        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\n"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['message'],"成功")
        self.assertEqual(response['status'],"1")

class B_Homepage_queryAccCategoryListByMemberCode(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress+"/mps-gateway/api/acct/queryAccCategoryListByMemberCode"
        self.test_data = {}
        self.acctType="1"

    def test(self):

        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\n"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['message'],"成功响应")
        self.assertEqual(response['status'],"1")



class B_Homepage_queryLatestAcsOrderInfo(TestCase):
    def setUp(self):
        self.loginUrl = domaimAddress+"/mps-gateway/api/index/queryLatestAcsOrderInfo"
        self.test_data = {}

    def test(self):

        print("request:\n"+json.dumps(self.test_data))
        #添加verify参数，防止SSL报错
        res=session.post(url=self.loginUrl,data=json.dumps(self.test_data),headers=headers,verify = False)
        response=res.json()
        print("response:\n"+str(response))
        self.assertEqual(response['code'],"00000000")
        self.assertEqual(response['message'],"成功响应")
        self.assertEqual(response['status'],"1")






































loginSuite=unittest.TestSuite()
loginSuite.addTest(A_Login("test"))
loginSuite.addTest(B_Homepage_announcement("test"))
loginSuite.addTest(B_Homepage_myaccount_merchant("test"))
loginSuite.addTest(B_Homepage_myaccount_operator("test"))
loginSuite.addTest(B_Homepage_mymenu("test"))
loginSuite.addTest(B_Homepage_pending_schedule("test"))
loginSuite.addTest(B_Homepage_menu_quick_entrance("test"))
loginSuite.addTest(B_Homepage_queryAccCategoryListByMemberCode("test"))
loginSuite.addTest(B_Homepage_queryLatestAcsOrderInfo("test"))





if __name__=='__main__':
    unittest.main(defaultTest='suite')
