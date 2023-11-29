import sqlite3
from userClass import User
from inventory import Inventory

class Cart:

    def __init__(self, databaseName="", tableName=""):
        self.databaseName = "databaseTables.db"
        self.tableName = "Cart"
        self.cart_items = []
        self.inventory = Inventory()

    def viewCart(self, userID):
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute("SELECT ISBN FROM Cart WHERE UserID = ?", (userID,))
        CartList = cur.fetchall()
        if not CartList:  
            print("Cart is empty")
        else:
            isbn_list = [str(item[0]) for item in CartList]  
            print(', '.join(isbn_list))  
        conn.close()

    def searchInv(self, ISBN):
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Inventory WHERE ISBN=?", (ISBN,))
        item = cur.fetchone()
        return item
    
    def addToCart(self, userID, ISBN):
        item = self.searchInv(ISBN)
        if item is None:
            print(f"Item with ISBN({ISBN}) not available.")
            return False

        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()

        # Check if the item is already in the cart
        cur.execute("SELECT Quantity FROM Cart WHERE UserID = ? AND ISBN = ?", (userID, ISBN))
        result = cur.fetchone()

        if result and result[0] is not None:
            # If the item is already in the cart and quantity is not NULL, increase the quantity
            new_quantity = result[0] + 1
            cur.execute("UPDATE Cart SET Quantity = ? WHERE UserID = ? AND ISBN = ?", (new_quantity, userID, ISBN))
        else:
            # If the item is not in the cart or quantity is NULL, insert it with quantity 1
            cur.execute("INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (?, ?, 1) ON CONFLICT(UserID, ISBN) DO UPDATE SET Quantity = Quantity + 1", (userID, ISBN))

        conn.commit()
        conn.close()

        print(f"Added item: {ISBN} to the cart")



    def removeFromCart(self, userID, ISBN):
        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Cart WHERE ISBN= ?", (ISBN,))
        item = cur.fetchall()
        if not item:  
            print("Item(ISBN:{ISBN}) is not found in cart.")
            return False
        else:
            cur.execute("DELETE FROM Cart WHERE UserID = ? AND ISBN = ?", (userID, ISBN))
        conn.commit()
        conn.close()
        return print(f"item(ISBN: {ISBN}) removed.")
        

    def checkOut(self, userID):
        print(f"Checkout: {userID}")

        conn = sqlite3.connect(self.databaseName)
        cur = conn.cursor()
        cur.execute("SELECT ISBN, Quantity FROM Cart WHERE UserID = ?", (userID,))
        items = cur.fetchall()

        # Iterate over items and decrease stock for each using the instance
        for ISBN, quantity in items:
            self.inventory.decreaseStock(ISBN, quantity)  # Call decreaseStock on the instance

        # Delete items from cart after checkout
        cur.execute("DELETE FROM Cart WHERE UserID = ?", (userID,))
        conn.commit()
        conn.close()

        print("Checkout completed.")