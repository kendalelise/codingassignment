import sqlite3
import sys

try:
    connection = sqlite3.connect("database.db")
    print("successful connection")

except:
    print("failed connection")

    sys.exit()

cursor = connection.cursor()

cursor.close()
connection.close()