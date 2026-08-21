def debug(function):
    def wrapper(*args, **kwargs):
        print(f"Parameters: args={args}, kwargs={kwargs}")
        result = function(*args, **kwargs)
        print(f"Return: {result}")
        return result
    return wrapper


@debug
def add(a, b):
    return a + b


# Test
add(3, 5)

def only_numbers(function):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"{arg} is not a number")
        result = function(*args, **kwargs)
        return result
    return wrapper


@only_numbers
def multiply(a, b):
    return a * b


# Test
print(multiply(4, 5))        # ambos números → funciona

try:
    print(multiply(4, "hello"))  # "hello" no es número → error
except TypeError as e:
    print(f"Error caught: {e}")

from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age = age - 1
        return age


# Test
user = User(date(1980, 11, 27))
print(f"Age: {user.age}")   

def adults_only(function):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User must be an adult (18+)")
        result = function(user, *args, **kwargs)
        return result
    return wrapper


@adults_only
def enter_bar(user):
    print(f"Welcome! Age {user.age} - Access granted")


# Test
adult = User(date(1980, 11, 27))    # 45 años → adulto
minor = User(date(2015, 5, 10))     # ~11 años → menor

enter_bar(adult)    # debe permitir

try:
    enter_bar(minor)    # debe lanzar error
except ValueError as e:
    print(f"Error caught: {e}")