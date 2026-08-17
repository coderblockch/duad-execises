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
