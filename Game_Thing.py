import random
number = random.randint(1, 15)
count = 5
while count > 0:
    guess = int(input(f'Guess a number from 1-15. You have {count} guesses left: '))
    if guess < number: print ('Too low!')
    elif guess > number: print ('Too high!')
    else: 
    print ("Your guess was correct!")
    break
    count -= 1
if guess != number: print ('You lost! Hahahahahahahahahahahaha nub go commit die')
