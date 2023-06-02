import mysql.connector
import hashlib

def login_user():
    username = input("Sisestage kasutajanimi: ")
    password = input("Sisestage parool: ")
    
    conn = mysql.connector.connect(
        host="sql7.freemysqlhosting.net",
        user="sql7622553",
        password="AU9aHcRCXb",
        database="sql7622553"
    )
    
    cursor = conn.cursor()
    
    # Hangib kasutaja andmed andmebaasist
    cursor.execute("SELECT password_hash, salt FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    
    if result is None:
        print("Kasutajanimi ei ole registreeritud.")
    else:
        password_hash, salt = result
        
        # Räsib sisestatud parooli koos soolaga
        input_password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        
        # Kontrollib parooli vastavust andmebaasis olevale räsi väärtusele
        if input_password_hash == password_hash:
            print("Sisselogimine õnnestus.")
        else:
            print("Vale parool.")
    
    conn.close()

login_user()








