import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

config = {
   
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'host': os.getenv('DATABASE_HOST'),
    'port': os.getenv('DATABASE_PORT'),
}


try:
    # Establish a connection to the database
    connection = mysql.connector.connect(**config)
    
    if connection.is_connected():
        print('Connected to the database!')
        # Perform any database operations here
        
except mysql.connector.Error as e:
    print(f'Error connecting to the database: {e}')

finally:
    # Close the connection when done
    if 'connection' in locals():
        connection.close()
        print('Connection closed.')
