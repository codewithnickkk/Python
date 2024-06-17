#Problem: Write a function that takes variable number of arguments and returns their sum.

def sum(num1=0, num2=0):
    return num1 + num2
n1 = int(input('enter num1: '))
n2 = int(input('enter num2: '))
print(sum(n1,n2))