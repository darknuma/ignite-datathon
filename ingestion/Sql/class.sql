CREATE TABLE Classes (
    Class_ID INT PRIMARY KEY,
    Class_Grade_ID INT,            -- Refers to SS1, SS2, SS3
    Discipline_ID INT,             -- Refers to Art (1), Commercial (2), Science (3), Tech (4)
    Subject_ID INT                 -- Refers to the Subject ID from the Subjects table
);
