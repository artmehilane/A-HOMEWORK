import mysql.connector
import hashlib
import os

def create_table():
    conn = mysql.connector.connect(
        host="sql7.freemysqlhosting.net",
        user="sql7622553",
        password="AU9aHcRCXb",
        database="sql7622553"
    )
    
    cursor = conn.cursor()
    
    # Loob tabeli kasutajate jaoks
    cursor.execute("""
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password_hash VARCHAR(64) NOT NULL,
            salt VARCHAR(32) NOT NULL
        )
    """)
    
    conn.commit()
    
    conn.close()

create_table()
