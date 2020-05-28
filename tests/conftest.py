#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

"""前后置共享文件"""


# 这样我们就定义了一个叫做 open_url 的 fixture
@pytest.fixture(scope='class') #定义scope的范围
def open_url():
    # 前置
    driver = webdriver.Chrome()
    driver.get(url='www.baidu.com') #url为链接地址
    yield driver    #yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()

# function：默认范围，每一个函数或方法都会调用，不填写时便是它
# 刷新页面 - 定义的第二个fixture
@pytest.fixture
def refresh_page(open_url):
    yield
    open_url.refresh()

# 直接将open_url作为了另一个fixture的前置引用进来，用yield隔开，当用例中执行完open_url前后置后，再执行了一次refresh的后置。
# 执行顺序： open_url yield 之前代码 – 用例代码 – open_url yield 之后代码 --》 refresh_page yield 之后代码
# 是不是很妙，可以解决许多用例流程环环相扣时的麻烦。

"删除商品分类"
@pytest.fixture(scope='function')  # 定义scope的范围
def del_title():
    print("-----前置开始执行function-----")
    if check_user(sql="SELECT * FROM commodity_category WHERE title = '测试图片1';"):
        del_user(sql="delete from commodity_category where title = '测试图片1';")
    yield  # yield之前代码是前置，之后的代码就是后置。
    print("-----后置开始执行function-----")
    if check_user(sql="SELECT * FROM commodity_category WHERE title = '测试图片1';"):
        del_user(sql="delete from commodity_category where title = '测试图片1';")

