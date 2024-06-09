import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Oto123456",
  database="test6"
)
mydata=mydb.cursor()
#mydata.execute("CREATE TABLE abc (a VARCHAR(255) , b VARCHAR(255) , c VARCHAR(255))")
#mydata.execute("SHOW TABLES")
test = ("INSERT INTO abc (a,b,c) VALUES (%s , %s , %s)")
value = ("a1" , "b1" , "c1")
mydata.execute(test,value)
#for data in mydata:
#    print(data)
mydata.execute('DELETE FROM abc WHERE a="a1"')
mydata.execute("SELECT * FROM abc ")
result = mydata.fetchall()
SQL = 'DROP TABLE abc'
# mydata.execute(SQL)
for a in result:
    print(a)
print(mydb)
