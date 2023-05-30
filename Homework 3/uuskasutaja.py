import mysql.connector
import hashlib
import os

def register_user():
    username = input("Sisestage kasutajanimi: ")
    password = input("Sisestage parool: ")
    print("Kasutaja registreeritud edukalt!")
    
    # Genereerib juhusliku soola
    salt = os.urandom(16).hex()
    
    # Räsib parooli koos soolaga
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    
    conn = mysql.connector.connect(
        host="sql7.freemysqlhosting.net",
        user="sql7622553",
        password="AU9aHcRCXb",
        database="sql7622553"
    )
    
    cursor = conn.cursor()
    
    # Lisab uue kasutaja andmebaasi
    cursor.execute("""
        INSERT INTO users (username, password_hash, salt)
        VALUES (%s, %s, %s)
    """, (username, password_hash, salt))
    
    conn.commit()
    
    conn.close()

register_user()
