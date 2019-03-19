import random
import numpy as np
import sys
import time

# roll_list = []


print("Welcome to the dice roll simulator!")
start = input("Start [Y/N] ")




def roll_function():

        for i in range(0, num_dice):
                roll = random.randint(1, faces)
                roll_list.append(roll)
        print("Rolling the dice...")
        time.sleep(2)
        print("The roll/s is/are:")
        print(roll_list)
        print("")
        print("The average roll is: " + str(np.average(roll_list)))
        time.sleep(5)
        print("")
        go_again()
        return roll_list


def go_again():
        response3 = input("Do you want to roll the same dice? \n [yes] \n [no] \n [Different Dice] \n")
        if response3 == "yes" or response3 == "y" or response3 == "Y":
                roll_list.clear()
                roll_function()
        elif response3 == "no" or response3 == "n" or response3 == "No":
                print("Thanks for using the simulator!")
        # elif response3 == "different dice" or response3 == "Different Dice":


if start == "Y" or start == "y":
        roll_list = []
        num_dice = int(input("How many dice do you want to roll? "))
        faces = int(input("How many faces do the dice have? "))
        roll_function()
elif start == "n" or start == "N":
        print("Thanks for using the simulator!")
        sys.exit()
else:
        print("Sorry I didn't understand that input.")