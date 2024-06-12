#Problem: Check if a number is prime.

number = int(input('enter a number: '))

is_prime = True

for i in range(2,number):
    if (number % i) == 0:
        is_prime = False
        break
print(is_prime)