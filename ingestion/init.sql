CREATE SCHEMA dwh

CREATE TABLE dwh.student_results (
    Result_ID SERIAL PRIMARY KEY, 
    Student_ID UUID,                 
    Class_Grade_ID INT, 
    Session INT,
    Subject VARCHAR(50),                 
    Score FLOAT                      
);
-- LOAD DATA
COPY dwh.student_results(Student_ID, Class_Grade_ID, Session, Subject, Score)
FROM '/data/student_results.csv'
delimiter ','
csv header;  


CREATE TABLE dwh.current_students (
    Student_ID UUID PRIMARY KEY,
    Gender VARCHAR(10),
    DOB DATE,
    Age INT,
    Class_Grade_ID INT,
    Discipline_ID INT,
    State_Of_Origin VARCHAR(50),
    Year_Of_Admission INT,
    Sports_House VARCHAR(50),
    Religion VARCHAR(50),
    Disability VARCHAR(3),
    Parent_Income_Level VARCHAR(50),
    Class_Prefect VARCHAR(3),
    Aspiring_Profession VARCHAR(100),
    Clubs TEXT[]
);
COPY dwh.current_students(Student_ID, Gender, DOB, Age, Class_Grade_ID, Discipline_ID, State_Of_Origin, Year_Of_Admission, Sports_House, Religion, Disability, Parent_Income_Level, Class_Prefect, Aspiring_Profession, Clubs)
FROM '/data/students_data.csv'
delimiter ','
csv header;


CREATE TABLE dwh.prev_jamb_results (
    Jamb_ID SERIAL PRIMARY KEY,
    Student_ID UUID,
    JAMB_Year INT,
    Admission_Year INT,
    JAMB_Score FLOAT,
    English FLOAT,
    Mathematics FLOAT,
    Physics FLOAT,
    Chemistry FLOAT,
    Literature FLOAT,
    Government FLOAT,
    Accounting FLOAT,
    Economics FLOAT,
    Biology FLOAT

);

COPY dwh.prev_jamb_results(Student_ID, JAMB_Year, Admission_Year, JAMB_Score, English, Mathematics, Physics, Chemistry, Literature, Government, Accounting, Economics, Biology
)
FROM '/data/jamb_results.csv'
delimiter ','
csv header;



CREATE TABLE dwh.prev_wassce_results (
    WASSCE_ID SERIAL PRIMARY KEY,
    Student_ID UUID,
    Year_Of_Admission INT,
    WASSCE_Year INT,
    Discipline_ID INT,
    Discipline VARCHAR(50),
    Aspiring_Profession VARCHAR(100),
    Gender VARCHAR(10),
    English CHAR(1),
    Mathematics CHAR(1),
    Civic_Education CHAR(1),
    ICT CHAR(1),
    Literature CHAR(1),
    Government_or_History CHAR(1),
    Religious_Studies CHAR(1),
    Language_yoruba_french_igbo CHAR(1),
    Bookkeeping CHAR(1),
    Economics CHAR(1),
    Accounting CHAR(1),
    Commerce CHAR(1),
    Marketing CHAR(1),
    Dyeing_and_Bleaching CHAR(1),
    Physics CHAR(1),
    Chemistry CHAR(1),
    Food_Nutrition CHAR(1),
    Biology CHAR(1),
    Electrical_Work CHAR(1),
    Agriculture CHAR(1),
    Technical_Drawing CHAR(1)
);

COPY dwh.prev_wassce_results(Student_ID,Year_Of_Admission,WASSCE_Year,Discipline_ID,Discipline,Aspiring_Profession,Gender,English,Mathematics,Civic_Education,ICT,Literature,Government_or_History,Religious_Studies, Language_Yoruba_French_Igbo,Bookkeeping,Economics,Accounting,Commerce,Marketing,Dyeing_and_bleaching,Physics,Chemistry,Food_Nutrition,Biology,Electrical_work,Agriculture,Technical_Drawing
)
FROM '/data/wassce_results.csv'
delimiter ','
csv header;


CREATE TABLE dwh.prev_wassce_students (
    WASSCE_ID SERIAL PRIMARY KEY,
    Student_ID UUID,
    Year_Of_Admission INT,
    WASSCE_Year INT,
    Discipline_ID INT,
    Discipline VARCHAR(50),
    Aspiring_Profession VARCHAR(60),
    Gender VARCHAR(10)
);

COPY dwh.prev_wassce_students(Student_ID, Year_Of_Admission, WASSCE_Year, Discipline_ID, Discipline, Aspiring_Profession, Gender)
FROM '/data/wassce_students.csv'
delimiter ','
csv header;


CREATE TABLE dwh.student_more_info (
    Info_ID SERIAL PRIMARY KEY,
    Student_ID UUID,
    Attendance_Rate FLOAT,
    Study_Hours INT,
    Subject_Struggle VARCHAR(50),
    Struggle_Scale INT,
    Class_Enjoyment INT,
    Understanding_Level INT
);

COPY dwh.student_more_info(Student_ID, Attendance_Rate, Study_Hours, Subject_Struggle, Struggle_Scale, Class_Enjoyment, Understanding_Level)
FROM '/data/student_more_info.csv'
delimiter ','
csv header;


CREATE TABLE dwh.student_subjects (
    Subject_ID SERIAL PRIMARY KEY,
    Student_ID UUID,
    Class_Grade_ID INT,
    Discipline_ID INT,
    Aspiring_Profession VARCHAR(100),
    Subjects TEXT[]
);
COPY dwh.student_subjects(Student_ID, Class_Grade_ID, Discipline_ID, Aspiring_Profession, Subjects)
FROM '/data/student_classes.csv'
delimiter ','
csv header;


CREATE TABLE dwh.current_student_historical_results (
    Student_ID UUID,
    Grade INT,            -- Refers to SS1, SS2, SS3
    Session INT,             -- Refers to First term to third term
    Subject VARCHAR(60) ,                -- Refers to the Subject
    Score FLOAT,
    Score_Type VARCHAR(60)
);
COPY dwh.current_student_historical_results(Student_ID, Grade, Session, Subject, Score, Score_Type)
FROM '/data/student_historical_results.csv'
delimiter ','
csv header;





