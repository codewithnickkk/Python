#day = str(input('day in the week: '))
#age = int(input('enter age: '))

#if (age > 17) & (day=='wednesday'):
#   print('ticket price = $10')
#elif (age > 17):
#   print('ticket price = $12')
#elif (age < 18) & (day=='wednesday'):
#    print('ticket price = $6')
#else:
#    print('ticket price = $8')
    
 
day = str(input('day in the week: '))
age = int(input('enter age: '))

price = 12 if age >=18 else 8

if day == 'wednesday':
    print(price-2)
else:
    print(price)
#compact coding 
