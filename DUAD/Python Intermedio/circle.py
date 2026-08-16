class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.1416 * self.radius * self.radius


my_circle = Circle(5)
print(my_circle.get_area())
