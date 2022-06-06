#This program will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random

#accept user input and save in a variable
names_string = input("Give me everybody's names, separated by a comma. ")

#seperate the names and save in a list using the string split method.
names = names_string.split(", ")

#select a random number between 0 and the len of the list.
payer_index = random.randint(0, len(names) - 1)

#select the person
payer_name = names[payer_index]
print(f'{payer_name} is going to buy the meal today!')
