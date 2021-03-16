#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors

# 打开数据库连接
db = pymysql.connect(host="114.119.182.20", port=6612, user="sunway_test", passwd="scfs_test@123!", db="scfscoredb",
                     charset='utf8', connect_timeout=3)
cursor = db.cursor()

sql = "select cust_name from tm_cust order by id desc limit 2;"
cursor.execute(sql)
data1 = cursor.fetchone()
data2 = cursor.fetchmany(3)
print ("data1:", data1)
print ("data2:", data2)
db.close()