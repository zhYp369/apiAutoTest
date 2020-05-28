# coding:utf-8
# heboqiang
import json
from base.method import Method, IsContent
from page.laGou import *
from page.CanShuHua import *
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
# import requests
# requests.packages.urllib3.disable_warnings()
from common.db import *
from common.logger import Log
import pytest

'''下面封装了get，post，dubbo请求的测试用例'''


class Test_Pytest():
    log = Log()

    def setup_class(self):
        print('类前面,我爱你')
        self.obj = Method()
        self.p = IsContent()
        self.execl = OperationExcel()
        self.operationJson = OperationJson()
        self.log = Log()

    def teardown_class(self):
        print('类之后')

    def setup_method(self):
        print('方法前面')

    #
    def teardown_method(self):
        print('方法后')

    # def isContent(self,r,row):
    #     # self.statusCode(r=r)
    #     assert self.p.isContent(row=row, str2=r.text)

    @pytest.mark.usefixtures("del_title")
    def test_addCategory_001(self):
        """添加商品分类校验"""
        print("test_laGou_001方法执行")
        self.log.info("-------添加商品分类：start!---------")
        r = self.obj.post(row=1, data=self.operationJson.getRequestsData(row=1))
        print("添加商品分类 is:", r.text)
        self.log.info("获取请求结果：%s" % r.text)
        # self.isContent(r=r, row=1)
        self.execl.writeResult(1, 'pass')
        assert r.status_code == 200
        assert str(r.json()["msg"]) == "成功"
        print("test_addCategory_0000001 is:", r.json()["data"]["id"])

# @pytest.mark.xfail
# def test_post_002(self,):
# 	print ("test_laGou_002方法执行")
# 	"测试post接口-参数化请求"
# 	self.log.info("------测试post接口-参数化请求：start!---------")
# 	r = self.obj.post(row=1,data=set_so_keyword1(phone='18821768014'),verify=False)
# 	print ("test_laGou_002 is:", r.text)
# 	self.isContent (r=r, row=1)
# 	self.execl.writeResult (1,'pass')
# 	assert r.status_code == 200
# 	print(r.status_code)

# def test_get_001(self):
# 	'''测试get接口'''
# 	r = self.obj.get(row=4,params=json.loads(self.operationJson.getRequestsData(4)))
# 	print(type(json.loads(self.operationJson.getRequestsData(4))))
# 	print(r.url)
# 	self.isContent(r=r, row=4)
# 	self.execl.writeResult(4, 'pass')
#
# def test_dubbo_003(self):
# 	'''测试dubbo'''
# 	r = self.obj.dubbo(row=5,param=self.operationJson.getRequestsData(5),method='tradeDetailQuery')
# 	# print(type(json.loads(self.operationJson.getRequestsData(5))))
# 	print (self.operationJson.getRequestsData(5))
# 	print(r.text)
# print (set_so_keyword(app_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))p_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))


if __name__=="__main__":
    pytest.main(['-s',r'E:\qjj_interface_auto1\tests\test_FenLeiGuanLi\test_01_TianJiaShangPinFenLei.py'])

