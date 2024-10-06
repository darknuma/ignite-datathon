from faker import Faker
import random
import datetime
import uuid


fake = Faker()

disciplines = {1: 'Art', 2: 'Commercial', 3: 'Science'}
states_of_origin = ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bayelsa",
                    "Benue", "Borno", "Cross River", "Delta",
                    "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT - Abuja", "Gombe",
                    "Imo", "Kaduna", "Kano", "Katsina", 
                    "Kebbi", "Kogi", "Kwara", "Lagos", "Ogun", "Ondo", "Osun",
                    "Oyo", "Plateau", 
                    "Rivers", "Sokoto", "Taraba"]
sports_houses = ["Red House", "Blue House", "Green House",
                  "Yellow House", "Brown House", "Purple House"]
religions = ["Christianity", "Islam"]
parent_income_levels = ["Low", "Middle Class", "Upper Class"]


aspiring_professions = {
    'Art': ['Artist', 'Writer', 'Fashion Designer', 'Actor', 'Journalist', 'Lawyer', 'Brand Specialist', 'Content Creator', 'Cook'],
    'Commercial': ['Business Executive', 'Accountant', 'Marketer', 'Entrepreneur', 'Economist', 'Auditor', ],
    'Science': ['Doctor', 'Pharmacist', 'Biologist', 'Scientist', 'Engineer', 'Agriculturist', 'Estate Manager'],
    'Technology': ['Software Developer', 'Engineer', 'Data Scientist', 'Technologist', 'Computer Scientist', 'Architect']
}


def generate_students(num_students):
    students = []
    for i in range(num_students):
        student_id = str(uuid.uuid4())  # Generate unique UUID for each student
        gender = random.choice(['Male', 'Female'])
        dob = fake.date_of_birth(minimum_age=12, maximum_age=17)
        age = datetime.datetime.now().year - dob.year
        grade = random.randint(1, 3)  # SS1, SS2, SS3
        discipline = random.randint(1, 3)  # Art, Commercial, Science
        state = random.choices(states_of_origin, weights=[0.2 if state in ["Lagos", "Ogun", "Oyo", "Osun"] else 0.8/32 for state in states_of_origin], k=1)[0],
        admission_year = 2020 + (3 - grade)  # Logic to set admission year based on class grade
        sports_house = random.choice(sports_houses) 
        religion = random.choice(religions) 
        disability = random.choices(["Yes", "No"], weights=[0.02, 0.98], k=1)[0]  # 98% have no disability
        parent_income = random.choices(parent_income_levels, weights=[0.1, 0.88, 0.02], k=1)[0]  # 10% low income, 2% upper class
        is_prefect = (grade == 3 and random.random() <= 0.015)  # 1.5% of SS3 students are prefects

        students.append({
            "Student_ID": student_id,
            "Gender": gender,
            "DOB": dob,
            "Age": age,
            "Class_Grade_ID": grade,
            "Discipline_ID": discipline,
            "State_Of_Origin": state,
            "Year_Of_Admission": admission_year,
            "Sports_House": sports_house,
            "Religion": religion,
            "Disability": disability,
            "Parent_Income_Level": parent_income,
            "Class_Prefect": "Yes" if is_prefect else "No"
        })
    return students

# Generate 2400 students (800 per class)
students = generate_students(1350)

subjects = {
    1: ["English", "Maths", "Civic Education", "ICT", "Literature", "Government", "Religious Studies", "Language (Yoruba, French, Igbo)"],
    2: ["English", "Maths", "Civic Education", "ICT", "Economics", "Accounting", "Commerce", "Marketing"],
    3: ["English", "Maths", "Civic Education", "ICT", "Physics", "Chemistry"],
}

optional_subjects = {8: ["Technical Drawing", "Food Nutrition" "Biology", "Agriculture", "Further Math"]}

trading_subjects = {
    5: "Bookkeeping",
    6: "Electrical work",
    7: "Dyeing and bleaching",
}

# english, maths, civic education and ICT are important courses.  
# each student are meant to select one trading subject, option 8 in trading subject should be optional for tech students
# all students are meant to do 9 courses


def generate_student_classes(students):
    student_classes = []
    for student in students:
        discipline = student['Discipline_ID']
        student_subjects = subjects[discipline]
        class_data = {
            "Student_ID": student['Student_ID'],
            "Class_Grade_ID": student['Class_Grade_ID'],
            "Discipline_ID": discipline,
            "Subjects": student_subjects
        }
        student_classes.append(class_data)
    return student_classes

student_classes = generate_student_classes(students)

for student in student_classes[:5]:
    print(student_classes)


def generate_session_results(students, sessions=3):
    results = []
    for session in range(1, sessions + 1):
        for student in students:
            for subject in student["Subjects"]:
                score = random.uniform(40, 100)  # Random score between 40 and 100
                result = {
                    "Student_ID": student["Student_ID"],
                    "Class_Grade_ID": student["Class_Grade_ID"],
                    "Session": session,
                    "Subject": subject,
                    "Score": round(score, 2)
                }
                results.append(result)
    return results

# Generate results for 3 sessions
results = generate_session_results(student_classes)


clubs = {
    1: ["Drama Club", "Music Club", "Press Club", "Fine Arts", "Debating Club"],
    2: ["Press Club", "Music Club", "Chess Club", "Debating Club", "Commerce Club"],
    3: ["JETS Club", "Red Cross", "Mathematics Olympiad Club", "Computer Club"],
    4: ["Computer Club", "JETS Club", "Red Cross", "Tech Club"]
}

# Assign clubs to each student
def assign_clubs(students):
    for student in students:
        discipline = student["Discipline_ID"]
        student["Clubs"] = random.sample(clubs[discipline], 2)  # Assign 2 random clubs
    return students

students_with_clubs = assign_clubs(students)
