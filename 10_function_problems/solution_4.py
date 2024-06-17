#Problem: Create a function that returns both the area and circumference of a circle given its radius.
#area pi*r^2
#circumference = 2*pi*r

import math

def area_circum(r):
    area = math.pi*r*r
    circumference = math.pi*r*2
    print('area: ',area)
    print('circumference: ',circumference)
    
r = float(input('enter radius of circle: '))
area_circum(r)
