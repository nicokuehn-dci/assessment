#!/usr/bin/env python3

# 1. Built-in Data Types
integer_num = 42  # int
float_num = 3.14  # float
is_python_fun = True  # bool
empty_value = None  # NoneType

# 2. Strings and Characters
single_char = 'A'  # Still a string, but length 1
greeting = "Hello, World!"  # A regular string

# 3. Comparison Operators
def compare_numbers():
    """
    This function compares two numbers and returns a string description.
    It demonstrates comparison operators and conditional statements.
    """
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{a} is less than {b}")
    else:
        print(f"{a} is equal to {b}")

# 4. Variable Names
def show_variable_names():
    snake_case_var = "I follow Python naming conventions"
    PascalCase = "I'm typically used for classes in Python"
    CONSTANT_VAR = 3.14159  # Constants are usually in ALL_CAPS
    print(f"snake_case_var: {snake_case_var}")
    print(f"PascalCase: {PascalCase}")
    print(f"CONSTANT_VAR: {CONSTANT_VAR}")

# 5. String Methods
def string_operations():
    """Demonstrate various string methods."""
    text = input("Enter a string: ")
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Stripped:", text.strip())
    print("Split:", text.split())
    print("Joined with hyphens:", "-".join(text.split()))

# 6. Function with Conditional Statements
def grade_score():
    """
    This function takes a numerical score and returns a letter grade.
    It demonstrates the use of if-elif-else statements.
    """
    score = float(input("Enter a score (0-100): "))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"A score of {score} gets a grade of: {grade}")

def menu():
    while True:
        print("\nPython Concepts Menu:")
        print("1. Compare Numbers")
        print("2. Show Variable Names")
        print("3. String Operations")
        print("4. Grade Score")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            compare_numbers()
        elif choice == '2':
            show_variable_names()
        elif choice == '3':
            string_operations()
        elif choice == '4':
            grade_score()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main execution
if __name__ == "__main__":
    menu()
