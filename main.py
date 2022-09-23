import mysql.connector
from mysql.connector import Error

pw = "password"

def create_server_connection(host_name, user_name, user_password):
    while True:
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                database="NSI",
                user=user_name,
                passwd=user_password
            )
            print("Connection Effectuée")
            cursor = connection.cursor()
            result = cursor.execute(input("SQL :"))
            print(cursor.fetchall())
        except Error as err:
            print(f"Error: '{err}'")
            

    return connection

connection = create_server_connection("164.132.67.138", "user", pw)