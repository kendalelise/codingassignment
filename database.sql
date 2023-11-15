-- users table
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Address TEXT NOT NULL,
    City TEXT NOT NULL,
    State TEXT NOT NULL,
    Zip TEXT NOT NULL,
    Payment TEXT
);

-- inventory table
CREATE TABLE Inventory (
    ISBN INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Genre TEXT NOT NULL,
    Pages INTEGER,
    ReleaseDate DATE,
    Stock INTEGER
);

--cart table
CREATE TABLE Cart (
    UserID INTEGER,
    ISBN INTEGER,
    Quantity INTEGER,
    PRIMARY KEY (UserID, ISBN),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ISBN) REFERENCES Inventory(ISBN)
);
