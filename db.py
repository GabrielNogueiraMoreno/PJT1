import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
