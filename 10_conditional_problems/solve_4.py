fruit = str(input('enter fruit: '))
shade = str(input('enter color_shade of fruit(eg: yellow, green, orange, brown): '))

if shade == 'yellow':
    print (fruit+' is ripe')
elif shade == 'green':
    print (fruit+' is unripe')
elif shade == 'orange':
    print (fruit+' is sweet')
elif shade == 'brown':
    print (fruit+' is overripe')
else:
    print(fruit+' is bad')