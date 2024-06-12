#Counting Positive Numbers
#Problem: Given a list of numbers, count how many are positive.
#numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_numbers_count = 0

for num in numbers:
    if num > 0:
        positive_numbers_count= positive_numbers_count+1 #also can be written as positive_numbers_count +=1
print(positive_numbers_count)