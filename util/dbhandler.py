import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="library"
    )
    return mydb

