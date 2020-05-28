
import pytest
import os


if __name__ == '__main__':

    # 定义测试集

    # args = ['-q','-s', 'E:\\zuixin--jiekou-aaa\\tests\\test_post002.py']
    start_dir = os.path.join((os.path.dirname(__file__)), 'tests')
    args = ['-q', '-s', start_dir]
    pytest.main(args)
