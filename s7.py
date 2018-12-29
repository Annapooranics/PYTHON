import sqlite3
db = sqlite3.connect('data1.db')
cursor = db.cursor()
cursor.execute('''SELECT * FROM users''')
for row in cursor:
    print ('−'*10)
    print ('ID:', row[0])
    print ('Name:', row[1])
    print ('Phone no:', row[2])
    print ('E-Mail id:', row[3])
    print ('Password:', row[4])
    print ('−'*10 )

