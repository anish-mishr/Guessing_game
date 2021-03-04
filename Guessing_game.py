#!/usr/bin/env python3

import random
# imports random module

num = random.randint(1,100) #generated random number between 1 and 100


"""INTRODUCTION OF GUESSING GAME"""

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

#list to store user guesses and tell about the number of trails later on

guesses = [0]

while True: 

    #takes user input as guess
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    #checks if guess is in between 1 and 100
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
        
    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('\t WARMER!')
        else:
            print('\t COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('\t WARM!')
        else:
            print('\t COLD!')
    
