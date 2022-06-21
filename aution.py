#A secret auction program
#importing the clear function to clear the console output
from replit import clear
#import and print auction logo
from art import logo
print(logo)
#dictionary to store the name and amount of bidders
auction_dictionary = {}
while True:
	name = input('What is your name?: ')
	bid_amount = int(input('What is your bid?: $'))
	continue_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
	auction_dictionary[name] = bid_amount
	#clear the console and continue taking bids.
	if continue_bid == 'yes':
		clear()
	#end the bid if there are no other bidders
	else:
		print('We will now display the winner for this bid...')
		break
#check the highest bidder and declare the winner
highest_bid = 0
for bidder, bid_amount in auction_dictionary.items():
	if bid_amount > highest_bid:
		highest_bid = bid_amount
print(f'The winner is {bidder} with a bid of ${highest_bid}.')
  
