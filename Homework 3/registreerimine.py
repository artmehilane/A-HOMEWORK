import mysql.connector

# Loob ühenduse andmebaasiga
conn = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7622553",
    password="AU9aHcRCXb",
    database="sql7622553"
)

# Sulgeb ühenduse
conn.close()



