import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Oto123456",
  database="test2"
)
mydata=mydb.cursor()

mydata.execute('SHOW TABLES')

for x in mydata:
    print(x)