#!user/bin/python
# coding:utf-8
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='123456',
                             db='cpay',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM cl_merchant_qrcode WHERE mch_id=1001"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()