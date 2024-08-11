n = 10
stars = 1
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end = '')
    for k in range(1):
        print('*'*stars)
        stars += 2

for i in range(n):
    for j in range(i):
        print(" ",end = '')
    for k in range(1):
        stars -= 2
        print('*'*stars)
        