import random
print("Welcome to the Sweets or Not Neat Guessing game! Win, and you walk off with some treats! However if you lose, you will suffer the consequences! To start,")
asdf = random.randint(1,15)
ree = input("Guess a random number from 1-15: ")
ree = int(ree)
if asdf == ree:
  print("Congratulations, you picked the right number! You win! Have a imaginary cookie!")
  quit()
elif asdf < ree:
  print("Ouch! Sorry, you guessed too high!")
elif asdf > ree:
  print("Oof! Sorry, you guessed too low!")
jojo = input("Try again, enter a number 1-15: ")
jojo = int(jojo)
if asdf == jojo:
  print("Congrats! You win! Have some imaginary cake!")
  quit()
elif asdf < jojo:
  print("Not quite, too high!")
elif asdf > jojo:
  print("Not so much, too low!")
nani = input("Last chance, enter a number 1-15: ")
nani = int(nani)
if asdf == nani:
  print("Wow, you clutched it! Pat yourself on the back and have some imaginary ice cream!")
else:
  print("Sorry, you failed all the trials, and you are banished to the shadow realm for 1000 years! Ponder your failures in exile!")
  quit()
print("The correct answer was:", asdf)
