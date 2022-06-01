'''
This program that checks if a given year is a leap year. 
A normal year has 365 days, leap years have 366, with an extra day in February.
Hint:
*On every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
***unless*** the year is also evenly divisible by 400

Flowchart: https://bit.ly/36BjS2D
'''
year = int(input("Which year do you want to check? "))

#method 1
if year % 4 == 0:
    if year % 100 != 0:
        print(f'Year {year} is a leap year.')
    elif year % 400 == 0:
        print(f'Year {year} is a leap year.')
    else:
        print(f'Year {year} is not a leap year.')
else:
    print(f'Year {year} is not a leap year.')

'''#method 2
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'Year {year} is a leap year.')
        else:
            print(f'Year {year} is not a leap year.')
    else:
        print(f'Year {year} is a leap year.')
else: 
    print(f'Year {year} is not a leap year.')'''

