'''
This program that checks if a given year is a leap year. 
A normal year has 365 days, leap years have 366, with an extra day in February.
Hint:
*On every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
***unless*** the year is also evenly divisible by 400

Flowchart: https://bit.ly/36BjS2D

It further returns the number of days in a month provided by the user.
'''

def is_leap_year(year):
    """Takes a year and return True if it is a leap year
    and False if it is not a leap year."""
    if year % 4 == 0:
        if year % 100 != 0:
            return True
            #print(f'Year {year} is a leap year.')
        elif year % 400 == 0:
            return True
            #print(f'Year {year} is a leap year.')
        else:
            return False
            #print(f'Year {year} is not a leap year.')
    else:
        return False
        #print(f'Year {year} is not a leap year.')

def days_in_month(year,month):
    """Returns the number of days in a month of a particular year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month entered."
    #if it is a leap year, set the number of days in February to 29
    if is_leap_year(year):
        month_days[1] += 1
        return(f'The number of days is {month_days[month - 1]}.')
    else:
        return(f'The number of days is {month_days[month - 1]}.')
        
check_year = int(input('Enter a year: '))
check_month = int(input('Enter a month: '))
days= days_in_month(year=check_year,month=check_month)
print(days)

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

