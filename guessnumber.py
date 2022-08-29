import random

def guess(x):
    randomnum = random.randint(1,x)
    guess = 0
    while guess != randomnum:
        guess = int(input(f'guess a number between 1 and {x}'))

        if  guess > randomnum:
            print(f"GUESS LOWER \n your guess: {guess} is higher than number")
        elif guess < randomnum:
            print(f"GUESS HIGHER \n your guess: {guess} is lower than number")
        else:
            guess == randomnum
            print(f"your guess {guess} is correct!")

guess(10)





