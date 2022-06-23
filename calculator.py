from multiprocessing.connection import answer_challenge
#A calculator program
from art import logo
print(logo)
#add function
def add(number1, number2):
	return number1 + number2
#subtract function
def subtract(number1, number2):
	return number1 - number2
#multiply function
def multiply(number1, number2):
	return number1 * number2
#divide function
def divide(number1, number2):
	return number1 / number2
#dictionary to store the operations
operations = {
	'+':add, 
	'-':subtract, 
	'*':multiply, 
	'/':divide
	}
def calculator():
	first_number = float(input("What's the first number?: "))
	for operator in operations:
		print(operator)
	while True:
		operator_input = input("Select an operator: ")
		second_number = float(input("What's the next number?: "))
		for operator, operator_name in operations.items():
			if operator == operator_input:
				answer = operator_name(number1=first_number, number2=second_number)
		print(f'{first_number} {operator_input} {second_number} = {answer}')
		if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ") == 'y':
			first_number = answer
		else:
			calculator()
calculator()
