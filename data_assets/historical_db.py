import random
import pandas as pd

# Load the previously saved current scores and students data
def load_current_scores(file_path):
    return pd.read_csv(file_path)

# Function to simulate historical scores with slight variations
def generate_historical_scores(current_scores, num_sessions):
    historical_scores = []
    for session in range(num_sessions):
        session_scores = []
        for score in current_scores:
            # Simulate learning improvement or deterioration
            variation = random.uniform(-5, 5)
            historical_score = max(min(score - variation, 100), 0)  # Ensure score is within 0 to 100
            session_scores.append(historical_score)
        historical_scores.append(session_scores)
    return historical_scores

# Generate student classes dynamically from the CSV file
def extract_student_classes(current_scores_df):
    student_classes = []
    grouped = current_scores_df.groupby('Student_ID')

    for student_id, group in grouped:
        class_grade_id = group['Class_Grade_ID'].iloc[0]  # Assume the grade is consistent for each student
        subjects = group['Subject'].unique().tolist()
        student_classes.append({
            "Student_ID": student_id,
            "Class_Grade_ID": class_grade_id,
            "Subjects": subjects
        })

    return student_classes

# Generate historical results for students in grades 2 and 3
def generate_historical_results(current_scores_df, sessions=3):
    student_classes = extract_student_classes(current_scores_df)
    student_results = []

    for student_class in student_classes:
        student_id = student_class["Student_ID"]
        grade = student_class["Class_Grade_ID"]
        subjects = student_class["Subjects"]

        # Filter the current scores from the loaded DataFrame
        current_scores = current_scores_df[current_scores_df["Student_ID"] == student_id]
        current_scores_only = current_scores["Score"].tolist()

        if not current_scores_only:
            print(f"No current scores found for Student_ID {student_id}. Skipping.")
            continue

        student_info = {
            "Student_ID": student_id,
            "Current_Grade": grade,
            "Current_Scores": current_scores.to_dict(orient='records')  # Store current scores
        }

        # Generate historical results if the student is in grade 3 or 2
        if grade == 3:
            # Simulate historical scores when they were in grade 2 and grade 1
            grade_2_scores = generate_historical_scores(current_scores_only, sessions)
            grade_1_scores = generate_historical_scores([score for session in grade_2_scores for score in session], sessions)
            
            student_info["Grade_2_Scores"] = {
                "Subjects": subjects,
                "Scores": grade_2_scores
            }
            student_info["Grade_1_Scores"] = {
                "Subjects": subjects,
                "Scores": grade_1_scores
            }

        elif grade == 2:
            # Simulate historical scores when they were in grade 1
            grade_1_scores = generate_historical_scores(current_scores_only, sessions)
            student_info["Grade_1_Scores"] = {
                "Subjects": subjects,
                "Scores": grade_1_scores
            }

        student_results.append(student_info)

    return student_results

# Main flow
if __name__ == "__main__":
    # Load previously saved current scores
    FILE_PATH = './csv_files/'
    current_scores_file = f"{FILE_PATH}student_results.csv"
    current_scores_df = load_current_scores(current_scores_file)

    # Use the dynamically generated student_classes to generate historical data
    historical_results = generate_historical_results(current_scores_df)

    # Prepare the historical results for CSV export
    rows = []
    for student in historical_results:
        student_id = student["Student_ID"]
        grade = student["Current_Grade"]
        
        # Save current scores
        for result in student["Current_Scores"]:
            rows.append({
                "Student_ID": student_id,
                "Grade": grade,
                "Session": result["Session"],
                "Subject": result["Subject"],
                "Score": result["Score"],
                "Score_Type": "Current"
            })

        # Save Grade 2 historical results
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

        # Save Grade 1 historical results
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

    # Save the historical results to CSV
    df = pd.DataFrame(rows)
    df.to_csv(f"{FILE_PATH}student_historical_results.csv", index=False)
    print("Student historical results have been saved to 'student_historical_results.csv'.")
