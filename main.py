# The task is this: the program will ask for the user's name and then it will say
# something like: “Well John, I've thought of a number between 1 and 100 and you
# have only eight tries to guess it. What number do you think it is?” On each try, the
# # player will say a number and the program can answer for different things.

# THE NUMBER IS 26
from random import randint
# ask for name and question
num=randint(0,100)

numOfTries = 0
name= input("what is your name? ")
while True:
  question= int(input("Well {}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is? ".format(name)))
  
  # 1 If the number the user said is less than 1 or greater than 100, it will tell them that  he/she has chosen a number that is out of play.
  if question<1 or question>100:
    print("{} has chosen a number that is out of play".format(name))
    numOfTries += 1
    print(numOfTries)


# 2 If the number the user chose is less than the number the program thought of, it will tell them that the answer is wrong, and that he/she chose a lower number than the secret number.
  if question<num:
    print("The answer is wrong, {} has chose a lower number than the secret number".format(name))
  numOfTries += 1
  print(numOfTries)

  
# 3 If the user chose a number greater than the secret number, it will let them know that it was greater.
  if question>num:
    print("The answer is wrong, {} has chose a greater number than the secret number".format(name))
    numOfTries += 1
    print(numOfTries)


# 4 And if the user got the secret number right, they will be informed that they have won,and how many tries that has taken them.
  if question == num:
    print("You chose the right number, you win!")
    print(f"Your attempts: {numOfTries}")
    break


# 5 If the user has not guessed correctly in their first attempt, they will be asked again to choose another number and so on until they win or until their eight attempts are done.\
  elif numOfTries == 8:
      print("Sorry, you ran out of tries!")
      break


# for i in range(1,9):
#  question != 26
#   print(try_again)
