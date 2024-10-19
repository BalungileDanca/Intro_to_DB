import mysql.connector
from mysql.connector import Error

def create_database():
        try:
                mydb = mysql.connector.connect(
                        host = "localhost"
                        user = "root"
                        password = "Balungile@321"
                    )

                if mydb.is_connected():
                        print("Successfully connected to the database server.")
                mycursor = mydb.cursor()

                sql = "CREATE DATABASE IF NOT EXISTS alx_book_python"
                mycursor.execute(sql)
                print("Database 'alx_book_store' created successfully!")
        except Error as e:
                print("Error while connecting to MYSQL:", e)
        finally:
                if 'mycursor' in locals() is not None:
                        mycursor.close()
                if 'mydb' in locals() and mydb.is_connected():
                        mydb.close()
                        print("Database connection closed.")
if __name__ == "__main__":
        create_database()





