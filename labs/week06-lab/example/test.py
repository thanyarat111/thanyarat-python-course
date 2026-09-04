#part 2
#Example 1

def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()

#ผลรัน
#Calling greet_person with different names:
#Hello, Alice! Nice to meet you.
#Hello, Bob! Nice to meet you.
#Hello, Charlie! Nice to meet you.

#Example 3

def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

#ผลรัน
#Calculating rectangle areas:
#Rectangle with length 5 and width 3
#Area = 5 × 3 = 15
#Rectangle with length 10 and width 7
#Area = 10 × 7 = 70

#part 3\
#Example 

def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()

#ผลรัน
#Using function that return values
#5 + 3 = 8
#10 + 7 = 17
#Sum of both results: 25


#Example 2
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    volumn = 4.0/3 * pi * radius
    return area, circumference, volumn

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

#ผลรัน
#Circle calculations:
#Circle with radius 5:
#Area: 78.54
#Circumference: 31.42
#volumn: 523.60


#part 4
#Example1
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

#ผลรัน
#Using default parameters:
#Hello, Mr./Ms. Smith!
#Hello, Dr. Johnson!
#Hello, Prof. Brown!

#Example 2
def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()

#ผลรัน
#Multiple default parameters:
#Profile: Alice, Age: 18, Country: Unknown
#Profile: Bob, Age: 25, Country: Unknown
#Profile: Charlie, Age: 30, Country: USA