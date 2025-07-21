# This code uses the pyinutplus library to validate user input.
# It prompts the user to enter the number of shopping bags and ensures that the input is a non-negative integer.
# If the input is valid, it prints the entered number.

import pyinputplus as pyip
result = pyip.inputInt("Enter the number of shopping bags:", min=0)
print(f"You have entered: {result}")

result = pyip.inputMenu(["red","blue","green"], lettered=True, numbered=False)
print(f"You have chosen a {result}, marker color.")

result = pyip.inputEmail("Enter your email address:")
print(f"You have entered: {result}")

try:
    number = int(input("Enter a number: "))
    result = 10/ number
    print("The result is:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:  
    print("Division by zero is not allowed. Please enter a non-zero number.")

years = [2010, 2019, 2000, 2021]
years.sort()
print(years)
assert years[0] <= years[1], "The first year should be less than or equal to the second year."