# coding:utf-8
#heboqiang
import pymysql
from configs.readCofig import *

# 获取连接方法
def get_db_conn():
    conn = pymysql.connect(host=host,            # 数据库地址
            port=3306,         # 端口（配置文件传入的是字符串格式，所以这里取值的时候，用getint的方法 ）
            user=user,            # 账号
            passwd=passwd,    # 密码
            database=db,    # 要操作的数据库名
            charset='utf8'
                           )# 指定编码格式

    return conn


# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    cur.execute(sql)  # 执行sql
    conn.commit()
    result = cur.fetchone()  # 获取所有查询结果
    print(result)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result  # 返回结果


# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        cur.execute(sql)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        conn.rollback()  # 回滚
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接0

# 封装常用数据库操作
def check_user(sql=None):
    # 注意sql中''号嵌套的问题
    # sql = "select * from user =  '{}' where phone = '{}'".format(user).format(name)
    # sql = "SELECT * FROM jp_user WHERE phone = '18821768014';"
    result = query_db(sql)
    return True if result else False
#
#
# def add_user(name, password):
#     sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
#     change_db(sql)
#
#
def del_user(sql=None):
    # sql = "delete from user where name='{}'".format(name)
    change_db(sql)

if __name__ == '__main__':
	check_user()

