from faker import Faker
import random
import pandas as pd
import duckdb
from datetime import date, timedelta



grades = {'SS1': 1, 'SS2': 2, 'SS3': 3}
disciplines = {'Art': 1, 'Commercial': 2, 'Science': 3, 'Technology': 4}
religions = ['Christian', 'Islam']
states_of_origin = ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta",
                    "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT - Abuja", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", 
                    "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", 
                    "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
clubs = ['Drama Club', 'Music Club', 'Press Club', 'Chess Club', 'Debating Club', 'Fine Arts', 'Homemakers Club', 
         'JETS Club', 'Red Cross', 'Computer Club', 'Mathematics Club']


aspiring_professions = {
    'Art': ['Artist', 'Writer', 'Fashion Designer', 'Actor', 'Journalist'],
    'Commercial': ['Business Executive', 'Accountant', 'Marketer', 'Entrepreneur', 'Economist'],
    'Science': ['Doctor', 'Pharmacist', 'Biologist', 'Scientist', 'Engineer',  'Software Developer', 'Engineer', 'Data Scientist', 'Technologist', 'Computer Scientist']
}

def admission_date(year):
    first_september = date(year, 9, 1)
    while first_september.weekday() > 4:
        first_september += timedelta(days=1)
    return first_september


def generate_students(count, grade, min_age, max_age, admission_year):
    students = []
    for i in range(count):
        # Select discipline and corresponding aspiring profession
        discipline = random.choice(list(disciplines.keys()))
        profession = random.choice(aspiring_professions[discipline])

        student = {
            'Student_ID': i + 1,
            # 'Name': fake.name(),  # Generate realistic Nigerian name
            'Class_Grade_ID': grades[grade],
            'Discipline_ID': disciplines[discipline],
            'Is_School_Prefect': random.choice(['Yes', 'No']),
            'Age': random.randint(min_age, max_age),
            'Gender': random.choice(['Male', 'Female']),
            'Nationality': 'Nigeria',
            'State_Of_Origin': random.choices(states_of_origin, weights=[0.2 if state in ["Lagos", "Ogun", "Oyo", "Osun"] else 0.8/32 for state in states_of_origin], k=1)[0],
            'Clubs_Interests': random.sample(clubs, k=random.randint(1, 3)),  # Randomized clubs (1 to 3 clubs)
            'Aspiring_Profession': profession,
            'DOB': date.today().replace(year=date.today().year - random.randint(min_age, max_age)),
            'Religion': random.choice(religions),
            'Has_Disability': random.choice(['Yes', 'No']),
            'Date_Of_Admission': admission_date(admission_year),
            'Year_Of_Admission': admission_year
        }
        students.append(student)
    return students

# Generating data for SS1, SS2, and SS3
ss1_students = generate_students(800, 'SS1', 12, 14, 2022)
ss2_students = generate_students(800, 'SS2', 13, 15, 2021)
ss3_students = generate_students(800, 'SS3', 14, 17, 2020)

# Combine all students into one DataFrame
students_df = pd.DataFrame(ss1_students + ss2_students + ss3_students)

students_df.to_csv("student_table")

# Load the data into DuckDB
con = duckdb.connect(database='students.db')
con.execute("CREATE TABLE IF NOT EXISTS students AS SELECT * FROM students_df")

# Check the first 5 rows
print(con.execute("SELECT * FROM students LIMIT 5").fetchall())
