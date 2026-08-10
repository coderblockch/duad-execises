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


def show_menu():
    print("=== STUDENT CONTROL SYSTEM ===")
    print("1. Add students")
    print("2. View all students")
    print("3. View top 3")
    print("4. View general average")
    print("5. Export to CSV")
    print("6. Import from CSV")
    print("7. Exit")

def get_student():
    name = input("Full name: ")
    section = input("Section (e.g. 11B): ")
    spanish = int(input("Spanish grade: "))
    english = int(input("English grade: "))
    social = int(input("Social studies grade: "))
    science = int(input("Science grade: "))
    return {
        "name": name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "social": social,
        "science": science
    }

def add_students(students):
    n = int(input("How many students? "))
    for i in range(n):
        print(f"--- Student {i + 1} ---")
        student = get_student()
        students.append(student)
    print("Students added!")
    return students

def view_students(students):
    if len(students) == 0:
        print("No students registered yet.")
        return
    for student in students:
        print("-" * 30)
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish: {student['spanish']}")
        print(f"English: {student['english']}")
        print(f"Social: {student['social']}")
        print(f"Science: {student['science']}")

def get_average(student):
    total = student['spanish'] + student['english'] + student['social'] + student['science']
    return total / 4


def view_top_3(students):
    if len(students) == 0:
        print("No students registered yet.")
        return
    ordered = sorted(students, key=get_average, reverse=True)
    print("=== TOP 3 STUDENTS ===")
    for student in ordered[:3]:
        average = get_average(student)
        print(f"{student['name']} ({student['section']}) - Average: {average}")

def get_general_average(students):
    if len(students) == 0:
        print("No students registered yet.")
        return
    total = 0
    for student in students:
        total = total + get_average(student)
    general = total / len(students)
    print(f"General average: {general}")


def import_csv(students):
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)                      # salta el encabezado
            for row in reader:
                student = {
                    "name": row[0],
                    "section": row[1],
                    "spanish": int(row[2]),
                    "english": int(row[3]),
                    "social": int(row[4]),
                    "science": int(row[5])
                }
                students.append(student)
        print("Data imported from students.csv")
    except FileNotFoundError:
        print("No CSV file found. Export data first.")
    return students


def main():
    students = []
    while True:
        show_menu()
        option = input("Choose an option: ")
        
        if option == "1":
            students = add_students(students)
        elif option == "2":
            view_students(students)
        elif option == "3":
            view_top_3(students)    
        elif option == "4":
            get_general_average(students)
        elif option == "5":
            export_csv(students)  
        elif option == "6":
            students = import_csv(students)      
        elif option == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()
