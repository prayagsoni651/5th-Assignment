# 2. Write a python script to get the last digit from a given number. (for example, if user
#    enters 2089 then your output should be 9)



number = int(input("Enter a number: "))

# get the last digit of the number
last_digit = number % 10

print(f"The last digit of the number is {last_digit}")
