import random

r = random.randint(0, 100) 

count = 0 #讓使用者可以計數，需要放在迴圈外，因為放迴圈內會歸零
while True:
	count += 1 #等同於 count = count + 1
	guess = input('Guess a number:')
	guess = int(guess) 
	if guess == r:
		print('You are right!', 'Times tried:', count)  
		break
	else: 
		if guess > r:
			print('Your guess is > r.', 'Times tried:', count, 'Try again!')

		elif guess < r:
			print('Your guess is < r.', 'Times tried:', count,  'Try again!')





