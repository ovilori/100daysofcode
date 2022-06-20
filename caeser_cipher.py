#Caeser cipher program.The Caesar cipher is a classic example of ancient cryptography and is said to have been used by Julius Caesar. 
#The Caesar cipher is based on transposition and involves shifting each letter of the plaintext message by a certain number of letters
#import the caeser cipher logo
from art import logo
#list to store the 26 letters of the alphabet 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#caeser cipher function that takes 'encode' or 'decode', the 'text' and 'shift' as inputs.
def caesar_cipher(input_text, shift_position, cipher_direction):
	#variable to store the final ecnrypted/decrypted text
	final_text = ''
	if cipher_direction == 'decode':
		shift_position *= -1
	for char in input_text:
		if char in alphabet:
			current_position = alphabet.index(char)
			new_position = current_position + shift_position
			if new_position < alphabet.index(min(alphabet)):
				new_position = new_position + len(alphabet)
				final_text += alphabet[new_position]
			elif new_position > alphabet.index(max(alphabet)):
				new_position = new_position - len(alphabet)
				final_text += alphabet[new_position]
			else:
				final_text += alphabet[new_position]
		else:
			final_text += char
	print(f'The {cipher_direction}d text is {final_text}.')
#Print the caesar cipher logo
print(logo)
while True:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	shift = shift % int(len(alphabet))
	#run the caesar function code above
	caesar_cipher(input_text=text, shift_position=shift, cipher_direction=direction)
	user_check = input("Type 'yes' if you want to repeat the program. Otherwise type 'no'.\n").lower()
	if user_check != 'yes':
		print('Goodbye.')
		break
	

