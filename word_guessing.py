# random module that will select random values
import random

# words list that will be picked up by random module
words = ["geeks", "haseeb"]

# the random word
word = random.choice(words)

# how many turns a user may have
turns = 12

# the guessed characters, if correct, will be stored in this variable
guess = ""

# while loop that runs the program unless the user have 0 turns left
while turns > 0:

    # how many times a user have failed will be stores in this variable
    fails = 0

    # this variable takes input from the user for guess word
    guessed = input("Please Enter Your Guess Word: ")

    # this stores the above entered guess word to guess variable 
    guess += guessed

    # this loop checks if the user entered word is correct
    for char in word:
        if char in guess:
            print(char, end=" ")

    # if not correct it will return a underscore and asks the user again for input
        else:
            print("_")

            # this updates the fails variable
            fails += 1
            
    # this checks if user have 0 fails 
    if fails == 0:

        # if the user have 0 fails it will tell them that they won
        print(f"You won. The Correct Word is {word}.")

        # this will break the while loop
        break
    
    # this block deals with the case in which guessed word is not found in randomly selected word
    if guessed not in word:

        # this tells the user they are wrong
        print("You are Wrong.")

        # this tells them how many turns they have left
        print(f"You have {turns} left.")

        # this will update turns variable and minus 1 from it
        turns -= 1

        # this deals if user have no turns left
        if turns == 0:
            print("You Loose. Better Luck Next Time.")
