import random

r = random.randint(0, 3) 


while True:
	guess = input('Guess a number:')
	guess = int(guess) 
	if guess == r:
		print('You are right!')
		break
	else: 
		if guess > r:
			print('Your guess is > r.')
			guess = input('Please try again:')

		elif guess < r:
			print('Your guess is < r.')
			guess = input('Please try again:')


