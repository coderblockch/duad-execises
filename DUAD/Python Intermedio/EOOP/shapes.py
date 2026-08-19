from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return self.side * self.side


# Test
sq = Square(5)
print(f"Square perimeter: {sq.calculate_perimeter()}")
print(f"Square area: {sq.calculate_area()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * 3.1416 * self.radius
    
    def calculate_area(self):
        return 3.1416 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height

    # Test all shapes
sq = Square(5)
ci = Circle(5)
re = Rectangle(4, 6)

print(f"Square - Perimeter: {sq.calculate_perimeter()}, Area: {sq.calculate_area()}")
print(f"Circle - Perimeter: {ci.calculate_perimeter()}, Area: {ci.calculate_area()}")
print(f"Rectangle - Perimeter: {re.calculate_perimeter()}, Area: {re.calculate_area()}")