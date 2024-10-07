import csv
import re


def fix_club_array_format(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        fieldnames = reader.fieldnames

        with open(output_file, "w", newline="", encoding="utf-8") as output_csvfile:
            writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                if row["Clubs"]:
                    row["Clubs"] = re.sub(r"\[(.*?)\]", r"{\1}", row["Clubs"])

                writer.writerow(row)


def replace_brackets_in_subjects(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        fieldnames = reader.fieldnames

        with open(output_file, "w", newline="", encoding="utf-8") as output_csvfile:
            writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                row["Subjects"] = re.sub(r"\[(.*?)\]", r"{\1}", row["Subjects"])

                writer.writerow(row)


def replace_spaces_in_headers(input_file, output_file):

    with open(input_file, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        headers = next(reader)

        updated_headers = [header.replace(" ", "_") for header in headers]

        with open(output_file, "w", newline="", encoding="utf-8") as output_csvfile:
            writer = csv.writer(output_csvfile)

            writer.writerow(updated_headers)

            for row in reader:
                writer.writerow(row)


input_file = "../csv_files/students_data.csv"  # Path to your input CSV file
output_file = "../students_data.csv"  # Path for the output fixed CSV file

input_subject = "../csv_files/student_classes.csv"
output_file_subject = "../student_classes.csv"

# replace_spaces_in_headers(input_subject, output_file_subject)
# Call the function to update the CSV
replace_brackets_in_subjects(input_subject, output_file_subject)

print("CSV headers updated successfully.")

# Call the function to fix the CSV
fix_club_array_format(input_file, output_file)
# fix_subjects_array_format(input_subject, output_file_subject)

print("CSV has been updated successfully.")
