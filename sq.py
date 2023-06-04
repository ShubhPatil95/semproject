import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# c.execute("""CREATE TABLE students(first_n TEXT, last_n TEXT, prn integer)""")
# c.execute("INSERT INTO students VALUES('chetan','jadhav',201106014)")
# c.execute("INSERT INTO students VALUES('Vinayak','Marathe',201106015)")
c.execute("SELECT * FROM students")
# c.execute("delete from students where first_n='chetan'")
print(c.fetchall())
conn.commit()
conn.close()
