import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )
    
    cursor = connection.cursor()
    
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as db_err:
        print(f"failed creating database: {db_err}")
        
except mysql.connector.Error as conn_err:
    print(f"Error connecting to Mysql: {conn_err}")
    
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close