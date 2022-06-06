#Rock, Paper and Scissors game - https://wrpsa.com/the-official-rules-of-rock-paper-scissors/.
#Rock wins against scissors
#Scissors win against paper.
#Paper wins against rock.
import random
from traceback import print_tb

#The rock is when you place your hand into the form of a simple fist.
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#The paper is when you place your hand in an outstretched position.
paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

#This is when you hold your fist with your index and middle finger pointing outwards in a V shape.
scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#saving the imagess in a list
rps_image = [rock, paper, scissors]

#ask the player to choose
playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f'You chose {playerChoice}: {rps_image[playerChoice]}')

#computer choice
computerChoice = random.randint(0, 2)
print(f'Computer chose {computerChoice}: {rps_image[computerChoice]}')

if playerChoice >= 3 or playerChoice < 0:
    print('Invalid number, you lose!')
elif playerChoice == 0 and computerChoice == 2:
    print('You win!')
elif playerChoice == 2 and computerChoice == 0:
    print('You lose.')
elif playerChoice > computerChoice:
    print('You win!')
elif playerChoice <  computerChoice:
    print('You lose.')
elif playerChoice == computerChoice:
    print('It is a tie.')
