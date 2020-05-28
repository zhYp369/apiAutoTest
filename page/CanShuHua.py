# coding:utf-8
#heboqiang

import  json
from utils.public import *
from utils.operationJson import  OperationJson
from utils.operationExcel import  OperationExcel
import pytest

operationJson=OperationJson()
operationExcel=OperationExcel()


"""**********************分类管理模块******************************"""
def addCategory(typeId=None):
    "编辑商品分类 类型id 1 积分商品分类 2 竞拍商品分类 3 寄拍商品分类 4 活动竞拍商品"
    data = json.loads(operationJson.getRequestsData(1))
    data["typeId"] = typeId
    return json.dumps(data)

def set_so_keyword1(phone=None):
    "获取请求参数"
    data = json.loads(operationJson.getRequestsData(1))
    data["phone"] = phone
    return json.dumps(data)
# print(type(set_so_keyword()))


def set_so_keyword(app_id=None,sign=None):
    "获取请求参数"
    data = json.loads(operationJson.getRequestsData(1))
    data["app_id"] = app_id
    data["sign"] = sign
    return json.dumps(data)
print(type(set_so_keyword()))

# print(set_so_keyword(app_id=20180829170725138653488,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))