#Problem: Write a generator function that yields even numbers up to a specified limit.

def generator(num):
    # for i in range(1, num+1):
    #     if i % 2 == 0:
    #         print(i)
    for i in range(2, num+1, 2): #(start, end, jump)
        print(i)
        
    #for i in range(2, num+1, 2): #(start, end, jump)
       # return i
            
    for i in range(2, num+1, 2): #(start, end, jump)
        yield i
        
for num in generator(10):
    print(num)