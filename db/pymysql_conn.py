#!/usr/bin/python3
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='tpay',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM pay_task WHERE id=59"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
