import sqlite3
from userClass import User

class Cart:

    def __init__(self, databaseName="", tableName=""):
        self.databaseName = "databaseTables.db"
        self.tableName = "Cart"
        self.cart_items = []

    def viewCart(self, userID, inventoryDatabase):
        print(f"View cart: {userID}\n")

        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.tableName} INNER JOIN {inventoryDatabase} ON {self.tableName}.item_id = {inventoryDatabase}.item_id WHERE user_id = ?", (userID,))
        cart_items = cur.fetchall()
        conn.close()

        return cart_items


    def addToCart(self, userID, ISBN):
        item = {"userID": userID, "ISBN": ISBN}
        self.cart_items.append(item)

        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute("INSERT INTO Cart (user_id, ISBN) VALUES (?, ?)", (userID, ISBN))
        conn.commit()
        conn.close()

        print(f"Added item: {ISBN} to the cart")

    def removeFromCart(self, userID, ISBN):
        print(f"Item to remove from cart: {ISBN}")

        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute("DELETE FROM Cart WHERE user_id = ? AND ISBN = ?", (userID, ISBN))
        conn.commit()
        conn.close()

        print(f"item({ISBN}) removed.")

    def checkOut(self, userID, inventory):
        print(f"Checkout: {userID}")

        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT ISBN, quantity FROM {self.tableName} WHERE user_id = ?", (userID,))
        items = cur.fetchall()

        for ISBN, quantity in items:
            inventory.decreaseStock(ISBN, quantity)

        cur.execute("DELETE FROM Cart WHERE user_id = ?", (userID,))
        conn.commit()
        conn.close()
        
        print("Checkout completed.")