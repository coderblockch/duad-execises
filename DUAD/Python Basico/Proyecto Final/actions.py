def get_valid_grade(subject):
    while True:
        try:
            grade = int(input(f"{subject} grade (0-100): "))
            if grade >= 0 and grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100. Try again.")
        except ValueError:
            print("That's not a valid number. Try again.")

def get_student():
    name = input("Full name: ")
    section = input("Section (e.g. 11B): ")
    spanish = get_valid_grade("Spanish")
    english = get_valid_grade("English")
    social = get_valid_grade("Social studies")
    science = get_valid_grade("Science")
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