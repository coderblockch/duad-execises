class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
    
    def get_average(self):
        total = self.spanish + self.english + self.social + self.science
        return total / 4


# Test
student = Student("David", "11A", 80, 90, 70, 60)
print(student.name)
print(student.get_average())