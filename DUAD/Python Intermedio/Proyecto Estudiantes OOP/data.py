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
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                student = Student(
                    row[0],
                    row[1],
                    int(row[2]),
                    int(row[3]),
                    int(row[4]),
                    int(row[5])
                )
                students.append(student)
        print("Data imported from students.csv")
    except FileNotFoundError:
        print("No CSV file found. Export data first.")
    return students