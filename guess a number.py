import random
number = random.randrange(0,100)
guessCheck = "wrong"
print("Welcome to Number Guess")

while guessCheck == "wrong":
	response=int(input("Please input a number between 0 and 100:"))
	if response < number:
		print("This is lower than actual number. Please try again.")
	elif response > number:
		print("This is higher than actual number. Please try again.")
	else:
		print("This is the correct number")
		guessCheck = "correct"

print("Thank you for playing Number Guess. See you again")
