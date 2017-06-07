"""This is a number guessing game ***Add more Comments***"""

from random import randint
from time import sleep

def get_user_guess():
    user_guess=int(raw_input("Guess a number: " ))
    return user_guess

def roll_dice(number_of_sides):
    first_roll=randint(1,number_of_sides)
    second_roll=randint(1,number_of_sides)
    max_val=number_of_sides*2
    print "This is a number guessing game.\n \nGuess a number that is betwen 1 and %d. \n \nTwo Dice will roll if your guess is higher than the sum of the two di you will win" % (max_val)
    sleep(1)
    user_guess=get_user_guess()
    if user_guess>max_val:
        print "You have guessed outside of the acceptable range"
        return
    else:
        print "Rolling..."
        sleep(2)
        print "%d" % (first_roll)
        sleep(1)
        print "%d" % (second_roll)
        sleep(1)
        total_roll=first_roll+second_roll
        print "%d" % (total_roll)
        print "Result..."
        sleep(1)
        if user_guess>total_roll:
            print "You've won"
            return
        else:
            print "You've lost"
            return

roll_dice(6)
