#  Task 0.
# The entire task is to be placed on GitHub (the name of public repository should be in group-number_student-id convention), after each task a commit is to be made to branch lab_3, and at the end a pull request is to be created with at least 1 person from the group invited in it.
# DONE

# Task 1: List Comprehensions
# Write a Python program that generates a list of squares of numbers from 1 to 10 using list comprehensions.ares)

newlist = [x ** 2 for x in range(1, 11)]
print("Task 1")
print(newlist)


# Task 2: Functions
# Expand the previous program by defining a function that takes a range of numbers as input and returns a list of squares for that range.e_squares(start, end))

def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


print("Task 2")
print(generate_squares(1, 10))


# Task 3: Classes
# Create a class called SquareGenerator that has a method to generate squares for a given range of numbers.

class SquareGenerator:
    def generate_squares(self,start, end):
        return [x ** 2 for x in range(start, end + 1)]


square_generator = SquareGenerator()
list_from_class = square_generator.generate_squares(1,10)
print("Task 3")
print(list_from_class)

# Task 4: Libraries
# Utilize the math library to calculate the square root of each number in the generated list from the previous task.

import math

square_root_of_square = [math.sqrt(x) for x in list_from_class]
print("Task 4")
print(square_root_of_square)


# Task 5: Exceptions
# Handle the case where the end of the range is less than the start in the SquareGenerator class.

class SquareGenerator:

    def generate_squares(self,start, end):
        if end < start:
            raise ValueError("End of the range must be greater than the start.")
        return [math.pow(x, 2) for x in range(start, end + 1)]


try:
    print("Task 5")
    square_generator = SquareGenerator()
    list_from_class = square_generator.generate_squares(10, 1)
except ValueError as e:
    print(e)

# Task 6: Modules
# Extract the SquareGenerator class into a separate module named square_generator.py.

import SquareGenerator as SG

square_generator1 = SG.SquareGenerator()
list_from_class = square_generator1.generate_squares(1,10)
print("Task 6")
print(list_from_class)

# Task 7: Packages
# Transform the square_generator module into a package by adding an empty __init__.py file and organize it accordingly.


# Task 8: Inheritance
# Create a subclass called CubicGenerator that inherits from the SquareGenerator class. Modify the CubicGenerator to generate cubes instead of squares.


# Task 9: Function Overriding
# Override the square generation method in the Cubic Generator class to generate squares with a check to see if the start of the range is less than the end, if not return an Exceptions


# Task 10: Abstract Elements
# Convert the SquareGenerator class into an abstract base class (ABC) using the abc module, making the generate_squares method abstract. Ensure that the CubicGenerator class implements this abstract method.


# Task 11:
# The result of the assignment should be a link to a pull request.
