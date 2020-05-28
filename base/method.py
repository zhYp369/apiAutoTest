# coding:utf-8
#heboqiang

# import dubbo_telnet
import  requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
import requests
requests.packages.urllib3.disable_warnings()
from configs.readCofig import *

operationExcel=OperationExcel()


def checkHeader(row,f1=None,f2=None):
	'''检测请求头'''
	url = operationExcel.getUrl(row=row)
	url = url.split('/')
	if url[4] == 'positionAjax.json?needAddtionalResult=false':
		return f1
	elif url[5] == 'byPosition.json':
		return f2


class Method:
	def __init__(self):
		self.operationJson = OperationJson()
		self.excel = OperationExcel()

	def post(self, row, data, **kwargs):
		self.uri = url
		try:
			r = requests.post(
				# 测试环境
				# url="http://192.168.3.15:83" + self.excel.getUrl(row=row),
				# 预发环境
				url=self.uri+self.excel.getUrl(row=row),
				data=data,
				headers=getHeadersValue(),
				verify=False,
				timeout=6)
			return r
		except Exception as e:
			raise  RuntimeError('接口请求发生未知的错误')

	def get(self,row,params=None,**kwargs):
		try:
			r=requests.get(
				url="http://192.168.3.15:83"+self.excel.getUrl(row=row),
				params=params,
				# headers=getHeadersValue(),
				timeout=6)
			return r
		except Exception as e:
			raise  RuntimeError('接口请求发生未知的错误')

	# def dubbo(self,row,param=None, method=None):
	# 	try:
	# 		Host = '192.168.1.203'  # Doubble服务器IP
	# 		Port = 28008  # Doubble服务端口
	# 		interface = self.excel.getUrl (row=row)
	# 		# 初始化dubbo对象
	# 		conn = dubbo_telnet.connect (Host, Port)
	# 		# 设置telnet连接超时时间
	# 		conn.set_connect_timeout (10)
	# 		# 设置dubbo服务返回响应的编码
	# 		conn.set_encoding ('gbk')
	# 		conn.invoke (interface, method, param)
	# 		command = 'invoke %s.%s(%s)' % (interface, method, param)
	# 		return conn.do(command)
	# 	except:
	# 		return Exception




    # def dubbo(self,row,param=None,Host=None, Port=None, interface=None, method=None):
    #     try:
    #         # 初始化dubbo对象
    #         conn = dubbo_telnet.connect (Host, Port)
    #         # 设置telnet连接超时时间
    #         conn.set_connect_timeout (10)
    #         # 设置dubbo服务返回响应的编码
    #         conn.set_encoding ('gbk')
    #         conn.invoke (interface, method, param)
    #         command = 'invoke %s.%s(%s)' % (interface, method, param)
    #         return conn.do(command)
    #     except:
    #         return Exception


	# def get(self,url,params=None,**kwargs):
	# 	r=requests.get(url=url,params=params,headers=getHeadersValue(),timeout=6)
	# 	return r

	# def post(self,row,data):
	# 	try:
	# 		r=requests.post(
	# 			url=self.excel.getUrl(row=row),
	# 			data=data,
	# 			headers=checkHeader(
	# 				row=row,
	# 				f1=getHeadersValue(),
	# 				f2=getHeadersInfo()),
	# 			timeout=6)
	# 		return r
	# 	except Exception as e:
	# 		raise  RuntimeError('接口请求发生未知的错误')

class IsContent:
	def __init__(self):
		self.excel=OperationExcel()

	def isContent(self,row,str2):
		flag=None
		if self.excel.getExpect(row=row) in str2:
			flag=True
		else:
			flag=False
		return flag

		print("https://api.hzxsoft.com"+self.excel.getUrl(row=1))
