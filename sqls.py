import sqlite3

conn = sqlite3.connect("jayesh.db")
c = conn.cursor()




command = input("Create\Insert\Display>>>")
if command.lower()=="create":
    c.execute("""CREATE TABLE storage(
    name TEXT,
    last TEXT,
    pay integer
    )""")
elif command.lower()=="insert":
    first_ = input("first_name : ")
    last_ = input("last_name : ")
    pay_ = int(input("pay :"))
    c.execute(f"INSERT INTO storage VALUES('{first_}','{last_}',{pay_})")
elif command.lower()=="display":
    tablename = input("table name :")
    c.execute(f"SELECT * FROM {tablename}")
    print(c.fetchall())
conn.commit()
conn.close()
