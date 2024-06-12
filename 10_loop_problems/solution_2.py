#Problem: Calculate the sum of even numbers up to a given number n.

n = int(input('enter n: '))

sum_of_even_nums = 0

for i in range(1, n+1):
    if i%2==0:
        sum_of_even_nums += i
print('sum of even num:',sum_of_even_nums)