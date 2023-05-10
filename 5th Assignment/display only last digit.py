#  7. Write a python script which takes a three digit number from the user and displays
#     only its last digit


number = int(input("Enter a three-digit number: "))

# extract the last digit of the number
last_digit = number % 10

print(f"The last digit of the number is {last_digit}")
