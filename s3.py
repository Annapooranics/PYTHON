import sqlite3
 # Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data1.db')
    # Get a cursor object
cursor = db.cursor()
#insert several users use executemany and a list with the tuples
users = [('anu','9867575', 'anu3@gmail.com', '874539hjg'),
         ('raj','6845784', 'raj56@gmail.com', 'fdgdg'),
         ('riya','75487879','riya3@gmail.com', 'dgft565')]
cursor.executemany(''' INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', users)
db.commit()
