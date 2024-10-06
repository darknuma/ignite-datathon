CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(100),
    Class_Grade_ID INT,          -- Refers to SS1 (1), SS2 (2), SS3 (3)
    Discipline_ID INT,           -- Refers to Art (1), Commercial (2), Science (3)
    Gender VARCHAR(10),
    Date_Of_Birth DATE,
    State_Of_Origin VARCHAR(50),
    Year_Of_Admission YEAR
);
