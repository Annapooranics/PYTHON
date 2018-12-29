import sqlite3
 # Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data.db')
    # Get a cursor object
cursor = db.cursor()
cursor.execute('''SELECT name, email, phone FROM users''')
user1 = cursor.fetchone() #retrieve the first row
print(user1[0],user1[1],user1[2]) #Print the first column retrieved(user's name)
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
