# 导入访问SQLite的模块
import sqlite3

# 1.打开或者创建数据库
# 也可以使用特殊名称 :memory: ,代表创建内存中的数据库
conn = sqlite3.connect('first.db')

# 2.获取游标
c = conn.cursor()

# 3.执行DDL语句创建数据表
c.execute('''create table user_tb(
    _id integer primary key autoincrement,
    name text,
    pass text,
    gender text)''')

# 执行DDL语句创建数据表
c.execute('''create table order_tb(
    _id integer primary key autoincrement,
    item_name text,
    item_price real,
    item_number real,
    user_id integer,
    foreign key(user_id) references user_tb(_id)
    )''')

# 4.关闭游标
c.close()
# 5.关闭连接
conn.close()