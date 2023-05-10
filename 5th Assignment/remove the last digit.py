# 1. Write a python script to remove the last digit from a given number. (for example, if
#    user enters 2534 then your output should be 253)


number = input("Enter a number: ")

# remove the last character (digit) from the number
number_without_last_digit = number[:-1]

print(f"The number without the last digit is {number_without_last_digit}")
