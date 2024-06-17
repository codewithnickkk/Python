# Problem: Create a lambda function to compute the cube of a number.

# def cube(number):
#     return number ** 3

# number = int(input('enter a number: '))
# print(cube(number))
cube = lambda x: x ** 3

number = int(input('enter a number: '))
print(cube(number))


