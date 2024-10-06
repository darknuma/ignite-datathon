import random
import uuid
import pandas as pd

def generate_students(num_students_per_year, admission_years):
    students = []
    for year in admission_years:
        for _ in range(num_students_per_year):
            student = {
                "Student_ID": str(uuid.uuid4()),
                "Year_Of_Admission": year,
                "Discipline_ID": random.randint(1, 3)
            }
            students.append(student)
    return students

# Function to generate JAMB results
def generate_jamb_results(students, jamb_years):
    jamb_results = []
    success_rate_increase = 0.05  # 5% increase in success rate per year

    for year_index, jamb_year in enumerate(jamb_years):
        base_success_rate = 0.7 + (year_index * success_rate_increase)
        admission_year = jamb_year - 3  # Students who write JAMB were admitted 3 years prior

        for student in students:
            if student['Year_Of_Admission'] == admission_year:
                discipline_id = student['Discipline_ID']

                if discipline_id == 1:  # Art
                    subjects = ['English', 'Mathematics', 'Literature', 'Government']
                elif discipline_id == 2:  # Commercial
                    subjects = ['English', 'Mathematics', 'Accounting', 'Economics']
                else:  # Science
                    subjects = ['English', 'Mathematics', 'Physics', 'Chemistry']
                    if random.random() < 0.5:
                        subjects[3] = 'Biology'  # 50% chance of Biology instead of Chemistry

                total_score = 0
                subject_scores = {}
                for subject in subjects:
                    base_score = random.uniform(50, 90)  # Base score between 50 and 90
                    score = min(100, base_score * (1 + random.uniform(0, 0.2)))  # Up to 20% increase
                    subject_scores[subject] = round(score, 2)
                    total_score += score

                if random.random() < base_success_rate:
                    total_score = min(337, total_score * random.uniform(1, 1.2))  # Up to 20% increase, max 337
                else:
                    total_score = total_score * random.uniform(0.8, 1)  # Up to 20% decrease

                jamb_result = {
                    "Student_ID": student['Student_ID'],
                    "JAMB_Year": jamb_year,
                    "Admission_Year": admission_year,
                    "JAMB_Score": round(total_score, 2),
                    **subject_scores  # Include individual subject scores in the result
                }
                jamb_results.append(jamb_result)

    return jamb_results


admission_years = [2018, 2019, 2020]  # Corresponding to JAMB years 2021, 2022, 2023
num_students_per_year = 150  # Adjust as needed
students = generate_students(num_students_per_year, admission_years)

jamb_years = [2021, 2022, 2023]
jamb_results = generate_jamb_results(students, jamb_years)

FILE_PATH = './csv_files/'
df_jamb_results = pd.DataFrame(jamb_results)
df_jamb_results.to_csv(f'{FILE_PATH}jamb_results.csv', index=False)

print("JAMB results have been saved to 'jamb_results.csv'.")
