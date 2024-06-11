#Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).
year = int(input('enter year: '))

if year%400 & year%100:
    print('leap year')
elif year%4:
    print('leap year')
else:
    print('not a leap year')