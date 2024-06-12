#Problem: Reverse a string using a loop.

string = str(input('enter sentence to reverse: '))

reversed_string = ''
norm_string = ''

for char in string:
    norm_string = norm_string + char
    reversed_string = char + reversed_string
print(norm_string,'\n',reversed_string)
