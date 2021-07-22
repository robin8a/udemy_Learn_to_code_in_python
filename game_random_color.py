import random

colors = ['red','blue','black','green','white']


while True:
    random_color = colors[random.randint(0,len(colors)-1)]    
    guess_color = input ("I'm thinking about a color, can you guess it? ")

    while True:
        if (random_color == guess_color.lower()):
            break
        else:
            guess_color = input ("Nope. Try again: ")
    print ( "You guessed it, I was thinking about:", random_color )
        
    play_again = input ("Let's play again (yes/no): ")

    if (play_again.lower() == 'no'):
        break
