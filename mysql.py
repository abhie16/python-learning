import mysql.

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234568'
)

myCursor = mydb.cursor()
myCursor.execute('show table')