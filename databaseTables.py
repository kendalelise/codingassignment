# databaseTables.py
import sqlite3

def setup_database():
    conn = sqlite3.connect("databaseTables.db")
    c = conn.cursor()

    # Create Users table
    c.execute("""CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Address TEXT NOT NULL,
        City TEXT NOT NULL,
        State TEXT NOT NULL,
        Zip TEXT NOT NULL,
        Payment TEXT
    )""")

    # Create Inventory table
    c.execute("""CREATE TABLE IF NOT EXISTS Inventory (
        ISBN INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        Author TEXT NOT NULL,
        Genre TEXT NOT NULL,
        Pages INTEGER,
        ReleaseDate DATE,
        Stock INTEGER
    )""")

    # Create Cart table
    c.execute("""CREATE TABLE IF NOT EXISTS Cart (
        UserID INTEGER,
        ISBN INTEGER,
        Quantity INTEGER,
        PRIMARY KEY (UserID, ISBN),
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (ISBN) REFERENCES Inventory(ISBN)
    )""")
    conn.commit()
    conn.close()
