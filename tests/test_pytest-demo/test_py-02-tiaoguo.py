#test_Pytest.py文件
#coding=utf-8

import pytest




class Test_Pytest():

        #pytest.xfail
        # 将该用例标记成xfail失败，并且该用例中的后续代码不会执行
        def test_one(self):
                print ("----start------")
                pytest.xfail (reason='该功能尚未完成')
                print ("test_one方法执行")
                assert 1 == 1

        def test_two(self):
                print ("test_two方法执行")
                assert "o" in "love"

        def test_three(self):
                print ("test_three方法执行")
                assert 3 - 2 == 1

        @pytest.mark.xfail标签

        #@pytest.mark.xfail
        #他的含义是期望测试用例是失败的，但是不会影响测试用例的的执行。如果测试用例执行失败的则结果是xfail（不会额外显示出错误信息）
        # 如果测试用例执行成功的则结果是xpass
        @pytest.mark.xfail
        def test_one1(self):
                print("test_one方法执行" )
                assert 1==2

        @pytest.mark.skip(reason="misunderstood the API")
        def test_two1(self):
                print("test_two方法执行" )
                assert "o" in "love"

        @pytest.mark.skipif(1==1,reason='跳过Test类，会跳过类中所有方法')
        def test_three1(self):
                print("test_three方法执行" )
                assert 3-2==1

if __name__=="__main__":
    pytest.main(['-s','test_Pytest.py'])
