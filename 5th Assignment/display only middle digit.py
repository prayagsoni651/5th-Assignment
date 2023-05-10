# 6. Write a python script which takes a three digit number from the user and displays
#    only its middle digit.




number = int(input("Enter a three-digit number: "))

# extract the middle digit of the number
middle_digit = (number // 10) % 10

print(f"The middle digit of the number is {middle_digit}")
