base ：封装请求方式比如：get post

common：封装数据库操作和日志的

configs：cfg存放数据库或者邮箱的数据，redconfig：用来读取操作

data：data.xls存放测试用例数据，requestData.json，从Excel取接口参数放这里 好修改

logs ：方日志
page：参数化操作

report：放测试报告 都是集成jenkins的allure

tests：测试用例，conftest.py，前后置共享文件

utils：操作Excel的

run：运行所以测试用例