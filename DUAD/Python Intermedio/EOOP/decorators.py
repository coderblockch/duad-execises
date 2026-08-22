from datetime import date


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


# --- Tests ---
add(3, 5)

print(multiply(4, 5))

try:
    print(multiply(4, "hello"))
except TypeError as e:
    print(f"Error caught: {e}")

user = User(date(1980, 11, 27))
print(f"Age: {user.age}")

adult = User(date(1980, 11, 27))
minor = User(date(2015, 5, 10))

enter_bar(adult)

try:
    enter_bar(minor)
except ValueError as e:
    print(f"Error caught: {e}")