CREATE TABLE Results (
    Result_ID INT PRIMARY KEY,
    Student_ID INT,                  -- Foreign Key to Students
    Session_ID INT,                  -- Foreign Key to Sessions
    Subject_ID INT,                  -- Foreign Key to Subjects
    Score FLOAT                      -- The result score for this student, session, and subject
);
