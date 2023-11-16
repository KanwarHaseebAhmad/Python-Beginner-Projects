import math
import random

# this will take the lowest number from user 
low = int(input("Please Enter the lowest number: "))

#this will take highest number from user
high = int(input("Please Enter the highest number: "))

#this will use random library to generate a random number between the lowest and highest number
random_int = random.randint(low, high)

# this will determine the number of turns needed to complete the game
number_of_guesses = round(math.log(high - low + 1, 2))

# this will count the number off guesses
count = 0

# this loop will run until count variable is less then the number of guesses needed for game
while count < number_of_guesses:

    # this will increment the count variable
    count += 1

    # this asks the user for their guess
    guess = int(input("Enter your Guess: "))

    # this block deals if you have successfully guessed the number and then breaks out of the while loop
    if random_int == guess:
        print(f"Congratulations! You have guessed right number in {count} tries.")
        break

    # this block checks if the number you have entered is lower then the random number
    elif random_int > guess:
        print("You have guessed too low.")

    # this block checks if the number is high then the random number 
    else:
        print("You have guessed too high")


# this deals if you have run out of number of guesses
if count >= number_of_guesses:
    print(f"the number is {random_int}. /n Better Luck Next Time")
