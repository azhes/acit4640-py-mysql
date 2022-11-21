import mysql.connector

db = mysql.connector.connect(
    host="database",
    user="admin",
    password="Password",
    database="backend"
)

c = db.cursor()

sql = "INSERT INTO backend.item (name, bcit_id) VALUES (%s, %s)"
val = ("Andrew", "A01265976")
c.execute(sql, val)

db.commit()

print("Data inserted.")