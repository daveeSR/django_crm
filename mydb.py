import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'supermaniscool'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE dj_crm_db")

print('db created')