import sqlite3
 # Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data1.db')
    # Get a cursor object
cursor = db.cursor()
user_id = 5
cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
user1 = cursor.fetchone()
print(user1[0],user1[1],user1[2])
