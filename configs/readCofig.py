# coding:utf-8
#heboqiang

import os
import configparser


cur_path = os.path.dirname(os.path.relpath(__file__))
configpath  = os.path.join(cur_path,"cfg.ini")
conf = configparser.ConfigParser()
conf.read(configpath,encoding="utf-8")

'''在这切环境'''
# #开发环境
# host = conf.get('mysql_kaifa','host')
# port = conf.get('mysql_kaifa','port')
# user = conf.get('mysql_kaifa','user')
# passwd = conf.get('mysql_kaifa','passwd')
# db = conf.get('mysql_kaifa','db')

# 测试环境
# url = conf.get('mysql_test','url')
# user = conf.get('mysql_test','user')
# passwd = conf.get('mysql_test','passwd')
# db = conf.get('mysql_test','db')

# # 预发布环境
# url = conf.get('mysql_prt','url')
# host = conf.get('mysql_prt','host')
# user = conf.get('mysql_prt','user')
# passwd = conf.get('mysql_prt','passwd')
# db = conf.get('mysql_prt','db')





# send_mail_1 = conf.get('email','send_mail')
# send_user_1 = conf.get('email','send_user')
# # login_1 = conf.get('email','login')
# to_user_1 = conf.get('email','to_user')
# send_mail_ren_1 = conf.get('email','send_mail_ren')


