# user class

class User:
    
    def __init__(self, databaseName=None, tableName=None):
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
        user_accounts = {}
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        if username in user_accounts:
            print("Username already exists. Please choose another one.")
            return

        user_accounts[username] = password

        print("Account created successfully!")
    
    def getLoggedIn(self):
        return self.loggedIn
    
    def getUserID(self):
        return self.userID
