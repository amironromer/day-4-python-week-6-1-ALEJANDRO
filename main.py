# The task is this: the program will ask for the user's name and then it will say
# something like: “Well John, I've thought of a number between 1 and 100 and you
# have only eight tries to guess it. What number do you think it is?” On each try, the
# # player will say a number and the program can answer for different things.

# THE NUMBER IS 26
from random import randint
from code import our_code
# ask for name and question
num=randint(0,100)

numOfTries = 0
name= input("what is your name? ")



our_code()

# for i in range(1,9):
#  question != 26
#   print(try_again)
