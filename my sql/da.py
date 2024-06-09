import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Oto123456",
  database="test2"
)
sql = "INSERT INTO cgpa (matric, name, cgpa) VALUES (%s, %s, %s)"
val = [
  ('1', 'Peter', '4'),
  ('2','Amy', '3'),
  ('3','Hannah', '1'),
  ('4','Michael', '2'),
  ('5','Sandy', '5'),
  ('6','Betty', '3'),
  ('7','Richard', '4'),
  ('8','Susan', '5'),
  ('9','Vicky', '2'),
  ('10','Ben', '4'),
]
mycursor = mydb.cursor()
mycursor.executemany(sql, val)


mydata=mydb.cursor()
#mydata.execute("SELECT * FROM cgpa ")
mydata.execute("UPDATE cgpa SET matric ='35' WHERE name = 'Amy'")
mydata.execute("SELECT * FROM cgpa ORDER BY name DESC LIMIT 5 OFFSET 2")
result = mydata.fetchall()
for X in result:
    print(X)
print(mydb)