import sqlite3
class Inventory:
    def __init__(self, databaseName="", tableName=""):
        self.databaseName = "databaseTables.db"
        self.tableName = "Inventory"

    def viewInventory(self):
        print(f"Inventory View: \n\n")
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.tableName}")
        inventory = cur.fetchall()
        conn.close()
        return inventory

    def searchInventory(self, title):
        print("Searching inventory...\n\n")
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.tableName} WHERE title LIKE ?", ('%' + title + '%',))
        results = cur.fetchall()
        conn.close()
        return results

    def decreaseStock(self, ISBN, quantity):
        print(f"Decreasing stock for ISBN '{ISBN}': \n")

        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"UPDATE {self.tableName} SET stock = stock - ? WHERE ISBN = ?", (quantity, ISBN))
        conn.commit()
        conn.close()
