#!/usr/bin/env python
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        port="3308",
        user="root",
        password="root",
        database="laravel",
    ) as connection:
        select_query = "SELECT * FROM users"
        with connection.cursor() as cursor:
            cursor.execute(select_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)

