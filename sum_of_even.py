#This program calculates the sum of all the even numbers from 1 to 100.
sum = 0
for number in range(0,101,2):
    sum += number
print(f'Sum of even numbers from 0 to 100 is {sum}.')

sum_even = 0
for number in range(0,101):
    if number % 2 == 0:
        sum_even += number
print(f'Sum of even numbers from 0 to 100 is {sum_even}.')


    