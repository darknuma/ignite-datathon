import random
from generate_db import generate_session_results, students, student_classes
import pandas as pd

def generate_historical_scores(current_scores, num_sessions):
    historical_scores = []
    for session in range(num_sessions):
        session_scores = []
        for score in current_scores:
            # Slightly reduce the scores in the past to simulate learning improvement
            variation = random.uniform(-5, 5)
            historical_score = max(
                min(score - variation, 100), 0
            )  # Ensure score is within 0 to 100
            session_scores.append(historical_score)
        historical_scores.append(session_scores)
    return historical_scores

# Generate current and historical student results
def generate_student_results(students, student_classes, sessions=3):
    student_results = []

    for student_class in student_classes:
        student_id = student_class["Student_ID"]
        grade = student_class["Class_Grade_ID"]
        subjects = student_class["Subjects"]

        current_scores = generate_session_results([student_class], sessions=sessions)

        # Extract only the scores from current session results
        current_scores_only = [result["Score"] for result in current_scores]

        student_info = {
            "Student_ID": student_id,
            "Current_Grade": grade,
            "Current_Scores": current_scores            
        }

        # If the student is in Grade 3, generate historical results for Grade 2 and Grade 1
        if grade == 3:
            grade_2_scores = generate_historical_scores(current_scores_only, sessions)
            grade_1_scores = generate_historical_scores(
                [score for session in grade_2_scores for score in session], sessions
            )
            student_info["Grade_2_Scores"] = {
                "Subjects": subjects,
                "Scores": grade_2_scores
            }
            student_info["Grade_1_Scores"] = {
                "Subjects": subjects,
                "Scores": grade_1_scores
            }

        # If the student is in Grade 2, generate historical results for Grade 1
        elif grade == 2:
            grade_1_scores = generate_historical_scores(current_scores_only, sessions)
            student_info["Grade_1_Scores"] = {
                "Subjects": subjects,
                "Scores": grade_1_scores
            }

        student_results.append(student_info)

    return student_results

# Generating historical results for the students
historical_results = generate_student_results(students, student_classes)

rows = []
for student in historical_results:
    student_id = student["Student_ID"]
    grade = student["Current_Grade"]
    
    for result in student["Current_Scores"]:
        rows.append({
            "Student_ID": student_id,
            "Grade": grade,
            "Session": result["Session"],
            "Subject": result["Subject"],
            "Score": result["Score"],
            "Score_Type": "Current"
        })

    if "Grade_2_Scores" in student:
        for session, scores in enumerate(student["Grade_2_Scores"]["Scores"], start=1):
            for subject, score in zip(student["Grade_2_Scores"]["Subjects"], scores):
                rows.append({
                    "Student_ID": student_id,
                    "Grade": 2,
                    "Session": session,
                    "Subject": subject,
                    "Score": score,
                    "Score_Type": "Historical_Grade_2"
                })

    if "Grade_1_Scores" in student:
        for session, scores in enumerate(student["Grade_1_Scores"]["Scores"], start=1):
            for subject, score in zip(student["Grade_1_Scores"]["Subjects"], scores):
                rows.append({
                    "Student_ID": student_id,
                    "Grade": 1,
                    "Session": session,
                    "Subject": subject,
                    "Score": score,
                    "Score_Type": "Historical_Grade_1"
                })


df = pd.DataFrame(rows)
FILE_PATH = './csv_files/'
df.to_csv(f"{FILE_PATH}student_historical_results.csv", index=False)

print("Student historical results have been saved to 'student_historical_results.csv'.")
