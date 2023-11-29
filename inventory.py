import sqlite3
class Inventory:
    def __init__(self, databaseName="", tableName=""):
        self.databaseName = "databaseTables.db"
        self.tableName = "Inventory"

    def viewInventory(self):
        print("Loading inventory...\n")
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.tableName}")
        inventory = cur.fetchall()
        conn.close()
        if not inventory:
            print("Inventory is empty.")
        else:
            for item in inventory:
                print(item)


    def searchInventory(self, title):
        print("Searching inventory...\n")
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.tableName} WHERE Title LIKE ?", ('%' + title + '%',))
        results = cur.fetchall()
        conn.close()
        if not results:
            print("Not found.")
            return False
        else:
            return print(results)

    def decreaseStock(self, ISBN, quantity):
        print(f"Decreasing stock for ISBN '{ISBN}': \n")

        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"UPDATE {self.tableName} SET stock = stock - ? WHERE ISBN = ?", (quantity, ISBN))
        conn.commit()
        conn.close()
