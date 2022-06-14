#Hangman game - player has 6 lives (attempt) to guess correctly the letters  in a randomly chosen word.
import random
from hangman_art import logo, stages
from hangman_words import word_list
#set the number of lives player has to 6.
lives = 6
#choose a random word from the list above
chosen_word = random.choice(word_list)
#store the length of chosen word
word_length = len(chosen_word)
#empty list to hold each letter the player will guess.
display = []
#variable to hold end of game
game_over = False
#display hangman logo
print(logo)
#For each letter in the chosen_word, add a "_" to the display list to represent each letter the player should guess.
for index in range(word_length):
	display.append('_')
#display to the player the number of characters and spaces to be guessed.
print(f"There are {word_length} characters in the word {' '.join(display)} to be guessed.")

#While there are still more letters to guess, ask the player repeatedly to guess a letter and assign their answer to a variable player_guess.
while not game_over:
	player_guess = input('Guess a letter: ').lower()
	#tell the player if they've already guessed a letter, print the letter and let them know.
	if player_guess in display:
		print(f"You've already guessed the letter - {player_guess}.")
	#Check if the letter the player guessed is one of the letters in the chosen_word. Loop through each position in the chosen_word,
	#If the letter at that position matches the letter guessed by the player, then reveal that letter in the display at that position.
	for index in range(word_length):
		if player_guess == chosen_word[index]:
			display[index] = player_guess
	#if the player guess is not in the chosen word, number of lives reduces by 1 and the game ends when the no of lives is zero
	if player_guess not in chosen_word:
		print(f"You guessed {player_guess}. This is not in the word. You lost a life!")
		lives -= 1
		if lives == 0:
			game_over = True
			print(f'You lost. The correct word is {chosen_word}.')
	print(''.join(display)) 
	#checks if the user guessed all letters correctly
	if '_' not in display:
		game_over = True
		print('You won!')
	#print the ASCII art from the stages list that corresponds to the current number of lives left.
	print(stages[lives])
