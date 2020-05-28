""""•@pytest.mark.last　　　　—最后一个执行
• @pytest.mark.run(order=1)—第几个执行


• 正常全部执行完成后才能停止，如果想遇到错误时停止测试: -x;也可以当用例错误个数n达到指定数量时，停止测试:- - maxfail=n
• 执行:
• pytest -x -v -s 文件名.py　　　　　　------- -x是遇到错误就停止
• pytest -x -v -s 文件名.py —maxfail=2　　------- --maxfail=2 是遇到两个错误就停止



**场景:
• 测试失败后要重新运行n次，要在重新运行之间添加延迟时 间，间隔n秒再运行。
• 执行:
• 安装:pip install pytest-rerunfailures
• pytest -v - -reruns 5 --reruns-delay 1 —每次等1秒 重试5次
"""
