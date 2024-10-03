#numberGuesser
import random

number = random.randrange(-1,11)

num_guess = 0
guess = -1

while guess != number :
    guess = (input("Guess the number I'm thinking of: "))
    num_guess+=1
    if guess.isdigit():
        guess = int(guess)
        if(guess > number):
            print("Too High!")
        else:
            print("Too Low")
        continue
    else:
        print("Write a number next time")
if(guess == number):
    print("You Got It In",num_guess,"guesses")
