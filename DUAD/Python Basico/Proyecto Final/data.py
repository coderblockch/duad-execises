import csv

def export_csv(students):
    if len(students) == 0:
        print("No students to export.")
        return
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "section", "spanish", "english", "social", "science"])
        for student in students:
            writer.writerow([
                student['name'],
                student['section'],
                student['spanish'],
                student['english'],
                student['social'],
                student['science']
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
                    student = {
                        "name": row[0],
                        "section": row[1],
                        "spanish": int(row[2]),
                        "english": int(row[3]),
                        "social": int(row[4]),
                        "science": int(row[5])
                    }
                except ValueError:
                    print(f"Skipping {row[0]}: grades are not valid numbers.")
                    continue
                imported.append(student)
    except FileNotFoundError:
        print("No CSV file found. Export data first.")
        return students
    if len(imported) == 0:
        print("The CSV file has no valid students. Keeping current data.")
        return students
    print("Data imported from students.csv")
    return imported