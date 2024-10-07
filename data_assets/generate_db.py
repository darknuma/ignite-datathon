from faker import Faker
import random
import datetime
import uuid
import pandas as pd
import csv
import re

fake = Faker()

disciplines = {1: "Art", 2: "Commercial", 3: "Science"}
states_of_origin = [
    "Abia",
    "Adamawa",
    "Akwa Ibom",
    "Anambra",
    "Bayelsa",
    "Benue",
    "Borno",
    "Cross River",
    "Delta",
    "Ebonyi",
    "Edo",
    "Ekiti",
    "Enugu",
    "FCT - Abuja",
    "Gombe",
    "Imo",
    "Kaduna",
    "Kano",
    "Katsina",
    "Kebbi",
    "Kogi",
    "Kwara",
    "Lagos",
    "Ogun",
    "Ondo",
    "Osun",
    "Oyo",
    "Plateau",
    "Rivers",
    "Sokoto",
    "Taraba",
]
sports_houses = [
    "Red House",
    "Blue House",
    "Green House",
    "Yellow House",
    "Brown House",
    "Purple House",
]
religions = ["Christianity", "Islam"]
parent_income_levels = ["Low", "Middle Class", "Upper Class"]


aspiring_professions = {
    "Art": [
        "Artist",
        "Writer",
        "Fashion Designer",
        "Actor",
        "Journalist",
        "Lawyer",
        "Brand Specialist",
        "Content Creator",
    ],
    "Commercial": [
        "Business Executive",
        "Accountant",
        "Marketer",
        "Entrepreneur",
        "Economist",
        "Auditor",
    ],
    "Science": [
        "Doctor",
        "Pharmacist",
        "Biologist",
        "Scientist",
        "Agriculturist",
        "Food Nutritionist",
        "Architect",
    ],
    "Technology": [
        "Software Developer",
        "Engineer",
        "Data Scientist",
        "Computer Scientist",
    ],
}


def generate_students(num_students):
    students = []

    for i in range(num_students):
        student_id = str(uuid.uuid4())  # Generate unique UUID for each student
        gender = random.choice(["Male", "Female"])
        dob = fake.date_of_birth(minimum_age=12, maximum_age=17)
        age = datetime.datetime.now().year - dob.year
        grade = random.randint(1, 3)  # SS1, SS2, SS3
        discipline_id = random.randint(1, 3)  # Art, Commercial, Science

        # Determine aspiring profession based on discipline
        discipline = disciplines[discipline_id]
        if discipline == "Science":
            profession = random.choice(
                aspiring_professions["Science"] + aspiring_professions["Technology"]
            )
        else:
            profession = random.choice(aspiring_professions[discipline])

        state = random.choices(
            states_of_origin,
            weights=[
                0.2 if state in ["Lagos", "Ogun", "Oyo", "Osun"] else 0.8 / 32
                for state in states_of_origin
            ],
            k=1,
        )[0]
        admission_year = 2020 + (
            3 - grade
        )  # Logic to set admission year based on class grade
        sports_house = random.choice(sports_houses)
        religion = random.choice(religions)
        disability = random.choices(["Yes", "No"], weights=[0.02, 0.98], k=1)[
            0
        ]  # 98% have no disability
        parent_income = random.choices(
            parent_income_levels, weights=[0.1, 0.88, 0.02], k=1
        )[
            0
        ]  # 10% low income, 2% upper class
        is_prefect = (
            grade == 3 and random.random() <= 0.015
        )  # 1.5% of SS3 students are prefects

        students.append(
            {
                "Student_ID": student_id,
                "Gender": gender,
                "DOB": dob,
                "Age": age,
                "Class_Grade_ID": grade,
                "Discipline_ID": discipline_id,
                "State_Of_Origin": state,
                "Year_Of_Admission": admission_year,
                "Sports_House": sports_house,
                "Religion": religion,
                "Disability": disability,
                "Parent_Income_Level": parent_income,
                "Class_Prefect": "Yes" if is_prefect else "No",
                "Aspiring_Profession": profession,  # Aspiring profession added
            }
        )
    return students


# Subject dictionary for each discipline
subjects = {
    1: [
        "English",
        "Maths",
        "Civic Education",
        "ICT",
        "Literature",
        "Government/History",
        "Religious Studies",
        "Language (Yoruba, French, Igbo)",
    ],
    2: [
        "English",
        "Maths",
        "Civic Education",
        "ICT",
        "Economics",
        "Accounting",
        "Commerce",
        "Marketing",
    ],
    3: ["English", "Maths", "Civic Education", "ICT", "Physics", "Chemistry"],
}

# # Optional subjects for Arts student based on profession
# opt_subjects = {
#     'Artist': "Fine Arts"

# }
# Optional subjects for Science students based on profession
optional_subjects = {
    "Doctor": "Biology",
    "Pharmacist": "Biology",
    "Biologist": "Biology",
    "Scientist": "Biology",
    "Engineer": "Further Maths",
    "Agriculturist": "Agriculture",
    "Food Nutritionist": "Food Nutrition",
    "Architect": "Technical Drawing",
    "Data Scientist": "Further Maths",
    "Computer Scientist": "Further Maths",
    "Software Developer": "Further Maths",
}

# Trade subjects - all students must pick one
trade_subjects = ["Bookkeeping", "Electrical work", "Dyeing and bleaching"]


# Function to assign subjects based on student discipline and profession
def generate_student_classes(students):
    student_classes = []

    for student in students:
        discipline_id = student["Discipline_ID"]
        aspiring_profession = student["Aspiring_Profession"]

        # Core subjects for all disciplines (English, Maths, Civic Education, ICT)
        core_subjects = ["English", "Maths", "Civic Education", "ICT"]

        discipline_subjects = subjects[discipline_id]

        # For Science students, assign optional subjects based on aspiring profession
        if discipline_id == 3:
            optional_subject = optional_subjects.get(aspiring_profession, None)
            if optional_subject:
                discipline_subjects.append(optional_subject)

        # Choose one trade subject
        trade_subject = random.choice(trade_subjects)

        # Total subjects (core + discipline + trade) should sum up to 9
        selected_subjects = (
            core_subjects + discipline_subjects[:5]
        )  # Take first 5 subjects from discipline
        if len(selected_subjects) < 8:
            selected_subjects.append(
                trade_subject
            )  # Ensure they have the trade subject
        
        # Ensure no duplicate core subjects
        discipline_subjects = [subj for subj in discipline_subjects if subj not in core_subjects]

        # Ensure the total number of subjects is 9 (core + discipline + trade subject)
        selected_subjects = core_subjects + discipline_subjects

    

        class_data = {
            "Student_ID": student["Student_ID"],
            "Class_Grade_ID": student["Class_Grade_ID"],
            "Discipline_ID": discipline_id,
            "Aspiring_Profession": aspiring_profession,
            "Subjects": selected_subjects[:8] + [trade_subject],  # Total of 9 subjects
        }

        student_classes.append(class_data)

    return student_classes


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
                    "Score": round(score, 2),
                }
                results.append(result)
    return results


clubs = {
    1: ["Drama Club", "Music Club", "Press Club", "Fine Arts", "Debating Club"],
    2: ["Press Club", "Music Club", "Chess Club", "Debating Club", "Commerce Club"],
    3: ["JETS Club", "Red Cross", "Mathematics Club", "Computer Club"],
    4: ["Computer Club", "JETS Club", "Red Cross", "Tech Club"],
}


def assign_clubs(students):
    for student in students:
        discipline = student["Discipline_ID"]
        student["Clubs"] = random.sample(clubs[discipline], 1) 
    return students


def save_students_to_csv(students, filename="students_data.csv"):
    headers = [
        "Student_ID", "Gender", "DOB", "Age", "Class_Grade_ID", "Discipline_ID", 
        "State_Of_Origin", "Year_Of_Admission", "Sports_House", "Religion", 
        "Disability", "Parent_Income_Level", "Class_Prefect", "Aspiring_Profession", "Clubs"
    ]
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def save_students_classes_to_csv(student_classes, filename="students_classes.csv"):
    headers = [
        "Student_ID", "Class_Grade_ID", "Discipline_ID", 
        "Aspiring_Profession", "Subjects"
    ]
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for student in student_classes:
            writer.writerow(student)

def save_students_results_to_csv(results, filename="students_results.csv"):
    headers = [
        "Student_ID", "Class_Grade_ID", "Session", 
        "Subject", "Score"
    ]
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for student in results:
            writer.writerow(student)
students = generate_students(1400)

student_classes = generate_student_classes(students)

results = generate_session_results(student_classes)

students_with_clubs = assign_clubs(students)
if __name__ == "__main__":
    FILE_PATH = "./csv_files/"

    save_students_to_csv(students_with_clubs, f"{FILE_PATH}students_data.csv")

    save_students_classes_to_csv(student_classes, f'{FILE_PATH}student_classes.csv')

    save_students_results_to_csv(results, f"{FILE_PATH}student_results.csv")
    

    # for student in results[:9]:
    #     print(student)
