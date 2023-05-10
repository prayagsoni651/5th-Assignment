# 3. Write a python script to swap data of two variables

# take input from the user for two variables
a = input("Enter the value of variable a: ")
b = input("Enter the value of variable b: ")

# print the initial values of the variables
print(f"Initial values: a = {a}, b = {b}")

# swap the values of the variables
a, b = b, a

# print the final values of the variables
print(f"Final values: a = {a}, b = {b}")
