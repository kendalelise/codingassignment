from user import User

class Cart:
    
    def __init__(self, databaseName="", tableName=""):
        self.databaseName = databaseName
        self.tableName = tableName
        self.cart_items = []

    def viewCart(self, userID, inventoryDatabase):
        print(f"View cart: {userID}")
        for item in self.cart_items:
            print(f"ISBN: {item['ISBN']}")

    def addToCart(self, userID, ISBN):
        item = {"userID": userID, "ISBN": ISBN}
        self.cart_items.append(item)
        print(f"Added item: {ISBN} to the cart")

    def removeFromCart(self, userID, ISBN):
        for item in self.cart_items:
            if item["userID"] == userID and item["ISBN"] == ISBN:
                self.cart_items.remove(item)
                print(f"Removed item: {ISBN} from the cart")

    def checkOut(self, userID, inventory):
        print(f"Checkout: {userID}")
        for item in self.cart_items:
            ISBN = item["ISBN"]
            inventory.decreaseStock(ISBN)
        self.cart_items = []
        print("Checkout completed.")