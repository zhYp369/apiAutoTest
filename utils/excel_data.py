#!/use/bin/env python
#coding:utf-8


class ExcelVariable:
	caseID=0
	url=4
	request_data=5
	expect=6
	result=7

def getCaseID():
	return ExcelVariable.caseID

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def get_request_data2():
	return ExcelVariable.request_data

def getExpect():
	return ExcelVariable.expect

def getResult():
	return ExcelVariable.result

def getHeadersValue():
	'''获取请求头'''
	headers={
		'Content-Type':'application/json',
		'access-token': '60bbb568f709419bac76d9ac247c0191'}
	return headers

print(getHeadersValue())

