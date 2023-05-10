# 9. Write a python script to use NOT IN operator to display the data not present in list


# define a list of values
my_list = [10, 20, 30, 40, 50]

# check if a value is not present in the list using the "not in" operator
value = int(input("Enter a value to check if it is not present in the list: "))
if value not in my_list:
    print(f"{value} is not present in the list")
else:
    print(f"{value} is present in the list")
