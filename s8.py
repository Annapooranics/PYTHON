import sqlite3
db = sqlite3.connect('data.db')
cursor = db.cursor()
cursor.execute('''SELECT * FROM users''')
#print(cursor.fetchall())
print (cursor.fetchmany(2))
