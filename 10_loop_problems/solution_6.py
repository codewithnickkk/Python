#Problem: Compute the factorial of a number using a while loop.

number = int(input('enter a number: '))

factorial = 1

while number > 0:
    factorial = number*factorial
    number=number-1
print(factorial)