# user class

class User:
    def __init__(self):
        self.userID = ''
        self.loggedIn = False
        self.databaseName = ''
        self.tableName = ''
    
    def __init__(self, databaseName, tableName):
        self.userID = ''
        self.loggedIn = False
        self.databaseName = databaseName
        self.tableName = tableName

    def login(self):
        input_userID = input("Enter your user ID: ")
        input_password = input("Enter your password: ")

        self.userID = input_userID
        self.loggedIn = True
        return True 
    
    def logout(self):
        self.userID = ''
        self.loggedIn = False
        return False
    
    def viewAccInfo(self):
        if self.loggedIn:
            print(f"Account information for user {self.userID}:")
        else:
            print("Please log in to view account information.")
    
    def createAcc(self):
        
        pass
    
    def getLoggedIn(self):
        return self.loggedIn
    
    def getUserID(self):
        return self.userID