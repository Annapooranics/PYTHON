import sqlite3
 # Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data1.db')
    # Get a cursor object
cursor = db.cursor()
newphone = '90087787'
userid = 5
cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
 (newphone, userid))
 
# Delete user with id 2
delete_userid = 3
cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
 
db.commit()
