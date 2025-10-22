import random as rnd

mystery_number = rnd.randint(1, 100)

def checkGuess(guess):
    while guess != mystery_number:
        while guess < 1 or guess > 100:
            guess = int(input("Guess a number between 1 and 100: "))
        if mystery_number > guess:
            if guess >= mystery_number-5 :
                print("Too low, you're getting hot!")
            else:
                print("Too low!")
            guess = int(input("Guess a number between 1 and 100: "))
        elif mystery_number < guess:
            if guess <= mystery_number + 5:
                print("Too high, you're getting hot!")
            else:
                print("Too high!")
            guess = int(input("Guess a number between 1 and 100: "))
    print(f"You guessed right! The mystery number was {mystery_number}. ")


print("Welcome to Guess the Number!")

userGuess = int(input("Guess the number between 1 and 100: "))
checkGuess(userGuess)









