#A Pizza order program for customer
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
#small pizza
if size == 'S':
    bill += 15
    print('Small Pizza is $15.')
    if add_pepperoni == 'Y':
        bill += 2
        print(' Pepperoni for Small Pizza is $2.')
#medium pizza
elif size == 'M':
    bill += 20
    print('Medium Pizza is $20.')
    if add_pepperoni == 'Y':
        bill += 3
        print('Pepperoni for Medium Pizza is $3.')
#larger pizza
elif size == 'L':
    bill += 25
    print('Large Pizza is $25.')
    if add_pepperoni == 'Y':
        bill += 3
        print('Pepperoni for Large Pizza is $3.')
if extra_cheese == 'Y':
    bill += 1
    print('Extra cheese is $1')
print(f'Your final bill is ${bill}.')