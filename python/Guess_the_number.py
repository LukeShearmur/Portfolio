
import random

guessestaken = 0 

#Guess the number game with randomly generated number between 1-20 

number = random.randint(1,20)
print("Hello, I am thinking of a number between 1-20")

for guessestaken in range (6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print ("Your guess is too low") 

    if guess > number:
        print ("Your guess is too high")

    if guess == number: 
        break

if guess == number:
    guessestaken = str(guessestaken + 1)
    print ("Good job, You guessed my number in " + guessestaken +" guesses!")

if guess != number:
    number = str(number)
    print ("Nope, the number I was thinking of was " + number + ".")





