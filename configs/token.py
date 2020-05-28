# """
# 获取token并返回给下一个函数的方法
# 1.调用登录接口，拿到获取的token
# 2.将拿到的token放在header中，调用确认登录接口
# 3.确认登录接口调用成功，接口返回信息正常
# """
# import requests
# import login
#
# headers = {"Content-Type": "application/json;charset=UTF-8"}
#
#
# def login():
#     """获取token"""
#     data = {"loginName": "***",
#             "loginPassword": "***"
#             }
#
#     # cookies = {"graphi_vcode_flag":"d21673e7-a903-41ad-8ca4-86fe7f9e9d46"}
#
#     url = "http://***/WebApi/PassCheck/LoginPassCheck"
#
#     r = requests.post(url=url, json=data, headers=headers)
#     # 将获取到的token返回
#     return (r.json()["data"]["token"])
#
#
# def confirm_login():
#     """调用获取登录信息接口，将登录成功后，返回的token放在该请求的header中"""
#     # 将login（）方法中返回的token放入header中
#     headers["Token"] = login()
#     r = requests.post(
#         url="http://***/WebApi/Designer/QueryDesignerBasicInfor",
#         headers=headers
#     )
#     print(r.headers)
#     print(r.json())
#
#
# confirm_login()
