#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

table = int(input('enter table to print: '))


for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(table, 'X' , i, '=', i*table)
