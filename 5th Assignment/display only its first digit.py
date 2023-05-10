# 5. Write a python script which takes a three digit number from the user and displays
#    only its first digit


number = int(input("Enter a three-digit number: "))

# extract the first digit of the number
first_digit = number // 100

print(f"The first digit of the number is {first_digit}")
