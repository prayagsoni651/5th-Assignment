# 8. Write a python script to use IN operator to display the data present in the list


# define a list of values
my_list = [10, 20, 30, 40, 50]

# check if a value is present in the list using the "in" operator
value = int(input("Enter a value to search in the list: "))
if value in my_list:
    print(f"{value} is present in the list")
else:
    print(f"{value} is not present in the list")
