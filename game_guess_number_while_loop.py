import random

number = random.randint(0,10)
guess = int ( input("I'm thinking about a number zero and ten? ") )

while True:
    if (number == guess):
        break
    else:
        guess = int ( input("No, try again: ") )

print ("You guessed it. I was thinking about: ", number)
