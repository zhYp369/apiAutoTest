# content of test_server.py

import pytest

#****************  一：使用自定义标记mark只执行部分用例

@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app
    #     print('1111')

def test_something_quick():
    pass

def test_another():
    pass

class TestClass:
    @pytest.mark.webtest
    def test_method(self):
        print('22222')

if __name__ == "__main__":
    pytest.main(["-s", "test_server.py", "-m=webtest"])
# 只运行用webtest标记的测试，cmd运行的时候，加个-m 参数，指定参数值webtest
#
# ```py
# pytest -v -m webtest

# 如果不想执行标记webtest的用例，那就用”not webtest”
# if __name__ == "__main__":
#     pytest.main(["-s", "test_server.py", "-m='not webtest'"])

# **************** 二：文件名类名方法执行部分用例
    # -v 指定的函数节点id
    # 如果想指定运行某个.py模块下，类里面的一个用例，如：TestClass里面testmethod用例
    # 每个test开头(或_test结尾)的用例，函数(或方法)的名称就是用例的节点id，指定节点id运行用-v 参数
    # pytest -v test_server.py::TestClass::test_method

    # 当然也能选择运行整个class
    # pytest - v test_server.py::TestClass

    # 也能选择多个节点运行，多个节点中间空格隔开
    # pytest -v test_server.py::TestClass test_server.py::test_send_http

#**************** 三：-k 组合调用执行部分用例
#     -k
#     匹配用例名称
#     可以使用 - k命令行选项指定在匹配用例名称的表达式
#
#     pytest - v - k
#     http
#     1
#     您也可以运行所有的测试，根据用例名称排除掉某些用例：
#
#     pytest - k “not send_http” -v
#     1
#     也可以同时选择匹配 “http” 和“quick”
#
#     pytest - k “http or quick” -v
