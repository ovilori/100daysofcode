#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give to the waiter/waitress? 10%, 12%, 15%? "))
people = int(input("How many people are splitting the bill? "))

bill_per_person = (bill/people) * (1 + tip/100)
#print(f"Each person will pay ${bill_per_person}")
print("Each person will pay ${:.2f}".format(round(bill_per_person, 2)))

