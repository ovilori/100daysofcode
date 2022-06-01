'''This program tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#setting the TRUE occurence to 0
true_count = 0
#settingthe LOVE occurence to 0
love_count = 0
#concatenating the strings together
name_together = (name1  + name2).lower()
t = name_together.count('t')
print(f'T occurs {t} times')
true_count +=t
r = name_together.count('r')
print(f'R occurs {r} times')
true_count +=r
u = name_together.count('u')
print(f'U occurs {u} times')
true_count +=u
e = name_together.count('e')
print(f'E occurs {e} times')
true_count +=e

l = name_together.count('l')
print(f'L occurs {l} times')
love_count +=l
o = name_together.count('o')
print(f'O occurs {o} times')
love_count +=o
v = name_together.count('v')
print(f'V occurs {v} times')
love_count +=v
e = name_together.count('e')
print(f'E occurs {e} times')
love_count +=e

#calculating the love score by concatenating the sum of TRUE count & LOVE count
love_score = int(str(true_count) + str(love_count))

#interpretation of the love score
if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <=50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')