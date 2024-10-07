import random
import pandas as pd

# Load student results DataFrame
student_results_file = './csv_files/student_results.csv'
student_results_df = pd.read_csv(student_results_file)

# Extract unique Student_IDs from student results
students = student_results_df['Student_ID'].unique()

# Likert scale from 1 (low) to 5 (high)
def generate_likert():
    return random.randint(1, 5)

# Generate classrooms and class sizes
def generate_classrooms():
    classrooms = []
    disciplines = ["Art", "Commercial", "Science", "Tech"]

    for grade in range(1, 4):  # SS1, SS2, SS3
        for discipline in disciplines:
            class_id = f"SS{grade}_{discipline}"
            class_size = 50  # Fixed for simplicity, you can vary it
            classrooms.append({"Class_ID": class_id, "Class_Size": class_size})

    return classrooms

# Generate student more info
def generate_student_more_info(students, student_results_df):
    student_more_info = []

    for student_id in students:
        attendance_rate = round(random.uniform(0.7, 1.0), 2)  # Between 70% to 100%
        study_hours = random.randint(1, 5)  # Study hours per prep time
        
        # Get the student's subject struggle from previous results
        subject_struggle_row = student_results_df[student_results_df["Student_ID"] == student_id]
        subject_struggle = subject_struggle_row['Subject'].mode()[0] if not subject_struggle_row.empty else random.choice(
            ["Maths", "English", "Physics", "Chemistry", "ICT"]
        )
        
        struggle_scale = generate_likert()
        class_enjoyment = generate_likert()
        understanding_level = generate_likert()

        student_more_info.append(
            {
                "Student_ID": student_id,
                "Attendance_Rate": attendance_rate,
                "Study_Hours": study_hours,
                "Subject_Struggle": subject_struggle,
                "Struggle_Scale": struggle_scale,
                "Class_Enjoyment": class_enjoyment,
                "Understanding_Level": understanding_level,
            }
        )

    return student_more_info

# Generate school info
def generate_school_info():
    school_info = {
        "Number_of_Classrooms": 12,  # 3 grades * 4 disciplines
        "Chemistry_Labs": 2,
        "Physics_Labs": 2,
        "Biology_Labs": 2,
        "Dye_Bleaching_Lab": 1,
        "Electrical_Lab": 1,
        "E_Library": 1,
        "Computer_Labs": 2,
        "Food_Nutrition_Lab": 1,
    }
    return school_info

# Generate classroom data
classrooms = generate_classrooms()

# Generate student more info data
student_more_info = generate_student_more_info(students, student_results_df)

# Generate school info
school_info = generate_school_info()

# Save to CSV
df_classrooms = pd.DataFrame(classrooms)
df_student_more_info = pd.DataFrame(student_more_info)
df_school_info = pd.DataFrame([school_info])  # Only one record, so wrap it in a list

# Saving the data into CSV files
FILE_PATH = './csv_files/'
df_classrooms.to_csv(f'{FILE_PATH}classrooms.csv', index=False)
df_student_more_info.to_csv(f'{FILE_PATH}student_more_info.csv', index=False)
df_school_info.to_csv(f'{FILE_PATH}school_info.csv', index=False)

print("Data has been saved to 'classrooms.csv', 'student_more_info.csv', and 'school_info.csv'.")
