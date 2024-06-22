#Problem: Create a recursive function to calculate the factorial of a number.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    # 5 * fac4
    # 4 * fac3
    # 3 * fac2
    # 2 * fac1
    # 1 * fac0
    # 0 => 1
print(factorial(5))