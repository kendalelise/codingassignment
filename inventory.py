class Inventory:
    def __init__(self, databaseName="", tableName=""):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewInventory(self):
        print(f"Viewing inventory from database '{self.databaseName}' and table '{self.tableName}'")

    def searchInventory(self):
        print("Searching inventory")

    def decreaseStock(self, ISBN):
        print(f"Decreasing stock for ISBN '{ISBN}'")
