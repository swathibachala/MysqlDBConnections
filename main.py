class Student:
    def __init__(selfself,name,age):
        self.name=name
        self.age=age
a=Student("swathi",32)

import pymysql

#opening DB connection
db=pymysql.connect(
    "localhost",
    "user",
    "pass",
    "dbname",
    3306
)

#cursor Object
cursor=conn.cursor
cursor.execute("IF Student table exists drop")
v=cursor.execute("create table student(name varchar(50))")
cursor.close()
conn.close()   