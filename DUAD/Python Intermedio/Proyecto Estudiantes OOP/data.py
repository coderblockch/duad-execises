import csv
from student import Student

def export_csv(students):
    if len(students) == 0:
        print("No students to export.")
        return
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "section", "spanish", "english", "social", "science"])
        for student in students:
            writer.writerow([
                student.name,
                student.section,
                student.spanish,
                student.english,
                student.social,
                student.science
            ])
    print("Data exported to students.csv")

def import_csv(students):
    imported = []
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) == 0:
                    continue
                if len(row) < 6:
                    print("Skipping a row with missing columns.")
                    continue
                try:
                    grades = [int(row[2]), int(row[3]), int(row[4]), int(row[5])]
                except ValueError:
                    print(f"Skipping {row[0]}: grades are not valid numbers.")
                    continue
                if min(grades) < 0 or max(grades) > 100:
                    print(f"Skipping {row[0]}: grades must be between 0 and 100.")
                    continue
                imported.append(Student(row[0], row[1], grades[0], grades[1], grades[2], grades[3]))
    except FileNotFoundError:
        print("No CSV file found. Export data first.")
        return students
    if len(imported) == 0:
        print("The CSV file has no valid students. Keeping current data.")
        return students
    print("Data imported from students.csv")
    return imported