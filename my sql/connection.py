import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Oto123456",
  database="test2"
)
mydata=mydb.cursor()
mydata.execute("SELECT * FROM customers")
result = mydata.fetchall()
for X in result:
    print(X)
print(mydb)
alltable = mydb.cursor()
alltable.execute("SHOW TABLES")
for table in alltable:
    print(table)

mycursor = mydb.cursor()



mycursor = mydb.cursor()

sql = "INSERT INTO cgpa (matric, name, cgpa) VALUES (%s, %s, %s)"
val = [
  ('Peter', '4'),
  ('Amy', '3'),
  ('Hannah', '1'),
  ('Michael', '2'),
  ('Sandy', '5'),
  ('Betty', '3'),
  ('Richard', '4'),
  ('Susan', '5'),
  ('Vicky', '2'),
  ('Ben', '4'),
  ('James', '2')
]

mycursor.execute(sql, val)

mydb.commit()




# alltable.execute("CREATE TABLE cgpa (matric VARCHAR(255), name VARCHAR(255), cgpa VARCHAR(255))")
# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()