import random

while True: 
	a = input('Enter one number:') 
	a = int(a)
	b = input('Enter a second number:') 
	b = int(b)
	if a > b:
		print('Wrong, the seonnd number must be larger than the first one.')
	else: 
		break

r = random.randint(a, b)

count = 0 #讓使用者可以計數，需要放在迴圈外，因為放迴圈內會歸零
while True:
	count += 1 #等同於 count = count + 1
	guess = input('Guess a number:')
	guess = int(guess) 
	if guess == r:
		print('You are right!', 'Times tried:', count)   
		break
	elif guess > r:
		print('Your guess is > r.')
	elif guess < r:
		print('Your guess is < r.')
	print('Times tried:', count, 'Try again!')





