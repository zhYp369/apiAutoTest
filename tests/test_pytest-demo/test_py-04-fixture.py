
import pytest

# @pytest.mark.usefixtures("open_url") #使用函数名为open_url的fixture
# @pytest.mark.usefixtures("refresh_page")


'''当用例需要调用fixture时，前面讲到可以直接在用例里加fixture参数，如果一个测试class都需要用到fixture，每个用例都去传参，会比较麻烦，这个时候，
可以在class外面加usefixtures装饰器，让整个class都调用fixture'''
'''
调用fixture的三种方法
1.函数或类里面方法直接传fixture的函数名称
2.使用装饰器@pyets.mark.usefixtures()修饰
3.autouse=True自动使用
'''

'''用例传fixture参数
方法一：先定义start功能 用例全部传start参数，调用该功能

'''

# import time
# import pytest
# import requests
#
# @pytest.fixture(scope="function")
# def start(request):
#     print("\n-----开始执行function-----")
#
# def test_a(start):
#     print("-----用例a执行-----")
#
# class Test_aaa():
#     def test_o1(self,start):
#         print("----用例01---------")
#
#     def test_02(self,start):
#         print("----用例02---------")
#
# if __name__ == '__main__':
#     pytest.main(["-s","usefixtures.py"])

'''
运行结果
usefixtures.py 
-----开始执行function-----
.-----用例a执行-----

-----开始执行function-----
.----用例01---------

-----开始执行function-----
.----用例02---------
'''

'''装饰器usefixtures
方法二：使用装饰器@pytest.mark.usefixtures()修饰需要运行的用例
'''

@pytest.fixture(scope="function")
def start():
    print("\n-----开始执行function------")

@pytest.mark.usefixtures("start")
def test_a():
    print("------用例a执行------")

@pytest.mark.usefixtures("start")
class Test_aaa():
    def test_01(self):
        print("------用例01-------")

    def test_02(self):
        print("------用例02-------")

if __name__ == '__main__':
    pytest.main(["-s","E:\qjj_interface_auto\\tests\\test_pytest-demo\\test_py-04-fixture.py"])

'''
叠加fixture
如果class用例需要同时调用多个fixture，可以使用@pytest.mark.usefixtures()叠加。注意叠加顺序，先执行的放底层，后执行的放上层
'''

# @pytest.fixture(scope="module")
# def first():
#     print("第一步：操作aaa")
#
# @pytest.fixture(scope="module")
# def second():
#     print("第二步：操作bbb")
#
# @pytest.mark.usefixtures("second")
# @pytest.mark.usefixtures("first")
# class TestFix():
#     def test_1(self):
#         print("用例1")
#         assert 1==1
#
#     def test_2(self):
#         print("用例2")
#         assert 2==2
# if __name__ == '__main__':
#     pytest.main(["-s","usefixtures.py"])

'''
usefixtures与传fixture区别
通过上面2个案例，对usefixtures使用基本方法已经掌握了，但是你会发现，我上面给的2个案例的fixture是没有返回值的。如果fixture有返回值，那么usefixtures就无法获取到返回值了，这个是它与用例直接传fixture参数的区别。
也就是说当fixture用return值需要使用时，只能在用例里面传fixture参数了。
当fixture没有return值的时候，两种方法都可以。

'''
'''当设置为True时，所有的test都会自动调用这个fixture。autouse遵循scope="关键字参数"规则：当scope="session"时，无论怎样定义只运行一次
；当scope="module"时，每个py文件只运行一次；当scope="class"时，每个class只运行一次（但是一个文件中包括function和class时，
会在每个function(不在class中)运行一次）；当scope="function"时，每个function运行一次；
'''
"""import pytest

@pytest.fixture(scope="module",autouse=True)
def start(request):
    print("\n----开始执行module------")
    print('module : %s'% request.module.__name__)
    print('------启动浏览器-------')
    yield
    print("------结束测试 end!----------")

@pytest.fixture(scope="function",autouse=True)
def open_home(request):
    print("function:%s \n--回到首页--"% request.function.__name__)

def test_01():
    print('----用例01-----')

def test_02():
    print('----用例02-----')

if __name__ == '__main__':
    pytest.main(["-s","autouse.py"])

"""
