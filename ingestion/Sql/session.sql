CREATE TABLE Sessions (
    Session_ID INT PRIMARY KEY,
    Class_Grade_ID INT,              -- Refers to SS1, SS2, SS3
    Session_Name VARCHAR(50),        -- e.g., "First Session", "Second Session"
    Year INT                         -- The academic year, e.g., 2023
);
