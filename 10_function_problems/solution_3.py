#Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# def multiply(value,factor):
#     return (value * factor)

# result = multiply((int(input('enter number or string to multiply: '))), (int(input('enter multiplying factor: '))))
# print(result)

def multiply(value, factor):
    try:
        factor = int(factor)
    except:
        return ('value must be an integer')
    try:
       value = float(value) if '.' in value else int(value)
    except:
        pass
    return ((value+' ') * factor)

result = multiply(input('enter number or string to multiply: '), input('enter multiplying factor: '))
print(result)


