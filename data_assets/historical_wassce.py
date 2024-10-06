import random
import uuid
from collections import defaultdict
import pandas as pd

def generate_students(num_students_per_year, admission_years):
    students = []
    for year in admission_years:
        wassce_year = year + 3  # WASSCE is typically taken 3 years after admission
        for _ in range(num_students_per_year):
            discipline_id = random.randint(1, 3)
            discipline = ['Art', 'Commercial', 'Science'][discipline_id - 1]
            aspiring_profession = random.choice(aspiring_professions[discipline])
            if discipline == 'Science' and aspiring_profession not in aspiring_professions['Science']:
                aspiring_profession = random.choice(aspiring_professions['Technology'])

            student = {
                "Student_ID": str(uuid.uuid4()),
                "Year_Of_Admission": year,
                "WASSCE_Year": wassce_year,
                "Discipline_ID": discipline_id,
                "Discipline": discipline,
                "Aspiring_Profession": aspiring_profession,
                "Gender": random.choice(['Male', 'Female'])
            }
            students.append(student)
    return students


def assign_subjects(student):
    discipline_id = student['Discipline_ID']
    aspiring_profession = student['Aspiring_Profession']

    core_subjects = ["English", "Mathematics", "Civic Education", "ICT"]
    discipline_subjects = subject_lists[discipline_id].copy()

    # For Science students, add profession-related optional subjects
    if discipline_id == 3:  # Science students
        optional_subject = optional_subjects.get(aspiring_profession, None)
        if optional_subject and optional_subject not in discipline_subjects:
            discipline_subjects.append(optional_subject)

    trade_subject = random.choice(trade_subjects)

    # Ensure no duplicate core subjects
    discipline_subjects = [subj for subj in discipline_subjects if subj not in core_subjects]

    # Ensure the total number of subjects is 9 (core + discipline + trade subject)
    selected_subjects = core_subjects + discipline_subjects

    if len(selected_subjects) > 8:
        selected_subjects = selected_subjects[:8]  # Limit to 8 subjects before adding trade
    selected_subjects.append(trade_subject)  # Total should now be 9

    return selected_subjects


def generate_wassce_result(subjects):
    grades = ['A', 'B', 'C', 'D', 'E', 'F']
    default_weights = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1]  # Adjust these weights as needed
    easy_subjects_weights = [0.2, 0.3, 0.3, 0.15, 0.05, 0.0]  # Higher weight for passing grades
    
    result = {}
    for subject in subjects:
        if subject in ['ICT', 'Civic Education']:
            grade = random.choices(grades, weights=easy_subjects_weights)[0]
        else:
            grade = random.choices(grades, weights=default_weights)[0]
        result[subject] = grade
    return result


# Constants
subject_lists = {
    1: ["English", "Mathematics", "Civic Education", "ICT", "Literature", "Government/History", "Religious Studies", "Language (Yoruba, French, Igbo)"],
    2: ["English", "Mathematics", "Civic Education", "ICT", "Economics", "Accounting", "Commerce", "Marketing"],
    3: ["English", "Mathematics", "Civic Education", "ICT", "Physics", "Chemistry"]
}

optional_subjects = {
    'Doctor': "Biology", 
    'Pharmacist': "Biology",
    'Biologist': "Biology",
    'Scientist': "Biology",
    'Engineer': "Further Maths",
    'Agriculturist': "Agriculture",
    'Food Nutritionist': "Food Nutrition",
    'Architect': "Technical Drawing",
    'Data Scientist': "Further Maths",
    'Computer Scientist': "Further Maths",
    'Software Developer': "Further Maths"
}

trade_subjects = ["Bookkeeping", "Electrical work", "Dyeing and bleaching"]

aspiring_professions = {
    'Art': ['Artist', 'Writer', 'Fashion Designer', 'Actor', 'Journalist', 'Lawyer', 'Brand Specialist', 'Content Creator'],
    'Commercial': ['Business Executive', 'Accountant', 'Marketer', 'Entrepreneur', 'Economist', 'Auditor'],
    'Science': ['Doctor', 'Pharmacist', 'Biologist', 'Scientist', 'Agriculturist', 'Food Nutritionist','Architect'],
    'Technology': ['Software Developer', 'Engineer', 'Data Scientist', 'Computer Scientist']
}

# Generate students
admission_years = [2018, 2019, 2020]  # Corresponding to WASSCE years 2021, 2022, 2023
num_students_per_year = 150 
students = generate_students(num_students_per_year, admission_years)

wassce_results = []
for student in students:
    subjects = assign_subjects(student)
    result = generate_wassce_result(subjects)
    wassce_results.append(result)


students_df = pd.DataFrame(students)
wassce_df = pd.DataFrame(wassce_results)

full_results_df = pd.concat([students_df, wassce_df], axis=1)

# Save to CSV files
FILE_PATH = './csv_files/'
students_df.to_csv(f'{FILE_PATH}wassce_students.csv', index=False)
full_results_df.to_csv(f'{FILE_PATH}wassce_results.csv', index=False)

print("Students and WASSCE results have been saved to 'wassce_students.csv' and 'wassce_results.csv'.")
