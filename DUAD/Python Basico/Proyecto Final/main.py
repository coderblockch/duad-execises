from menu import show_menu
from actions import add_students, view_students, view_top_3, get_general_average
from data import export_csv, import_csv

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