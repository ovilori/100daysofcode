############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
import re
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card(deck):
	"""Returns a random card from the deck."""
	card = random.choice(deck)
	return card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

for i in range(2):
	user_cards.append(deal_card(deck=cards))
	computer_cards.append(deal_card(deck=cards))
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(card_list):
	"""Takes a list of cards and returns the sum."""
	total = sum(card_list)
	#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
	if total == 21 and len(card_list) == 2:
		return 0

	#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
	if 11 in card_list and total > 21:
		card_list.remove(11)
		card_list.append(1)
	return total

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user, computer):
	"""Compares the user and computer scores."""
	if user_score == computer_score:
		return 'It is a draw.'
	elif computer_score == 0:
		return 'You lost. Computer has a Blackjack.'
	elif user_score == 0:
		return ' You have a Blackjack. You won.'
	elif user_score > 21:
		return 'You went over. lost.'
	elif computer_score > 21:
		return 'Computer went over. You won.'
	elif user_score > computer_score:
		return 'You have a greater score. You won.'
	else:
		return 'Computer has a greater score. You lost.'

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
while True:
	user_score = calculate_score(user_cards)
	computer_score = calculate_score(computer_cards)
	print(f"Your cards: {user_cards} and current score: {user_score}.")
	print(f"Computer's first card: {computer_cards[0]} and current score: {computer_score}")

	if user_score == 0 or computer_score == 0 or user_score > 21:
		print('Game over')
		break

	#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
	else:
		user_input = input("Do you want to draw another card (type 'y' for yes or 'n' for no)?: ").lower()
		if user_input == 'y':
			user_cards.append(deal_card(deck=cards))
		else:
			print('Game over')
			break

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
	computer_cards.append(deal_card(deck=cards))
	computer_score = calculate_score(computer_cards)
	print(f"Your final cards: {user_cards} and final score: {user_score}.")
	print(f"Computer's final cards: {computer_cards} and final score: {computer_score}.")

#compare user and computer score
print(compare(user=user_cards,computer=computer_cards))
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

