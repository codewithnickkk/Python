#Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
#items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "mango"]

for i in items:
    #print(i)
    if items.count(i) == 1:
        continue
    else:
        print(i)
        break