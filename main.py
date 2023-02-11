import random
import math

# Taking input for lower range and upper ranger
lowerRange = int(input("Enter a numer for lower range: "))
upperRange = int(input("Enter a number for upper range: "))

# Initializing and printing number of chances the user has to guess
numOfLife = round(math.log(upperRange - lowerRange + 1, 2))
print(
    f"\nYou have {numOfLife} lives to guess the number!\nGuess a number between {lowerRange} and {upperRange} to win the game!"
)

# Generating a random number between lowerRange & upperRange
randomNum = random.randint(lowerRange, upperRange)

# Intializing total number of guesses
totalGuesses = 0

# Looping through the while loop untill user guesses the number in predefined numer of chances
while totalGuesses < numOfLife:
    totalGuesses += 1

    # Taking input for the guess
    guess = int(input("\nGuess a number: "))

    # Checking the guess number
    match guess:
        case _ if guess == randomNum:
            print(f"You guessed the number correctly using {totalGuesses} live(s)")
            break
        case _ if guess < randomNum:
            print(f"You guessed too low, Aim high!\nYou have {numOfLife - totalGuesses} live(s) left")

        case _ if guess > randomNum:
            print(f"You guessed too high, A little lower please!\nYou have {numOfLife - totalGuesses} live(s) left")

# Print that user failed to guess after exiting the loop
else:
    print(f"You have exhausted all your lives! The random number was {randomNum}")
