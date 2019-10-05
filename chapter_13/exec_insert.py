# 导入访问SQLite的模块
import sqlite3

conn = sqlite3.connect('first.db')

c = conn.cursor()

c.execute('insert into user_tb values (null, ?, ?, ?)',('孙悟空', '123456', 'male'))
c.execute('insert into order_tb values (null, ?, ?, ?, ?)',('鼠标', '34.2', '3', 1))

conn.commit()

c.close()

conn.close()