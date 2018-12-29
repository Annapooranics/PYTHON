import sqlite3
 # Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data1.db')
    # Get a cursor object
cursor = db.cursor()
name1 = 'Surya'
phone1 = '43545'
email1 = 'surya@example.com'
password1 = '$3%^34'
 
name2 = 'priya'
phone2 = '9045845'
email2 = 'doe@example.com'
password2 = 'abc'
 
# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
print('First user inserted')
 
# Insert user 2
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
print('Second user inserted')
 
db.commit()
