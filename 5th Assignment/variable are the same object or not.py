'''10. Write a python script to use IS operator to display if both variables are the same
object or not?'''


# define two variables with the same value
a = [1, 2, 3]
b = [1, 2, 3]

# check if the variables are the same object using the "is" operator
if a is b:
    print("a and b refer to the same object")
else:
    print("a and b do not refer to the same object")
