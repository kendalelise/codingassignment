import sqlite3
from userClass import User
from inventory import Inventory

class Cart:
    
    def __init__(self, databaseName="", tableName=""):
        self.databaseName = "database.db"
        self.tableName = "Cart"
        self.cart_items = []

    def viewCart(self, userID, inventoryDatabase):
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.tableName} INNER JOIN {inventoryDatabase} ON {self.tableName}.item_id = {inventoryDatabase}.item_id WHERE user_id = ?", (userID,))
        cart_items = cur.fetchall()
        conn.close()
        return cart_items

    def addToCart(self, userID, ISBN):
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute("INSERT INTO Cart (user_id, ISBN) VALUES (?, ?)", (userID, ISBN))
        conn.commit()
        conn.close()

    def removeFromCart(self, userID, ISBN):
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute("DELETE FROM Cart WHERE user_id = ? AND ISBN = ?", (userID, ISBN))
        conn.commit()
        conn.close()

    def checkOut(self, userID, inventory):
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT ISBN, quantity FROM {self.tableName} WHERE user_id = ?", (userID,))
        items = cur.fetchall()

        for ISBN, quantity in items:
            inventory.decreaseStock(ISBN, quantity)

        cur.execute("DELETE FROM Cart WHERE user_id = ?", (userID,))
        conn.commit()
        conn.close()