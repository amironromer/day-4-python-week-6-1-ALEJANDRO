# The task is this: the program will ask for the user's name and then it will say
# something like: “Well John, I've thought of a number between 1 and 100 and you
# have only eight tries to guess it. What number do you think it is?” On each try, the
# # player will say a number and the program can answer for different things.

# THE NUMBER IS 26

# ask for name and question
num=26

numOfTries = 0
name= input("what is your name? ")
question= int(input("Well {}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is? ".format(name)))
try_again= int(input("Try again, input another number: "))
# 1 If the number the user said is less than 1 or greater than 100, it will tell them that  he/she has chosen a number that is out of play.
if question<1:
  print("{} has chosen a number that is out of play".format(name))
  numOfTries += 1
  print(numOfTries)
  print(try_again)
elif question>100:
  print("{} has chosen a number that is out of play".format(name))
  numOfTries += 1
  print(numOfTries)
  print(try_again)
# 2 If the number the user chose is less than the number the program thought of, it will tell them that the answer is wrong, and that he/she chose a lower number than the secret number.
elif question<26:
  print("The answer is wrong, {} has chose a lower number than the secret number".format(name))
  numOfTries += 1
  print(numOfTries)
  print(try_again)
  
# 3 If the user chose a number greater than the secret number, it will let them know that it was greater.
elif question>26:
  print("The answer is wrong, {} has chose a greater number than the secret number".format(name))
  numOfTries += 1
  print(numOfTries)
  print(try_again)

# 4 And if the user got the secret number right, they will be informed that they have won,and how many tries that has taken them.
if question == 26:
  print("You chose the right number, you win!")
  print("Your attempts: {numOfTries}")
  break
elif numOfTries == 8:
      print("Sorry, you ran out of tries!")
      break


# 5 If the user has not guessed correctly in their first attempt, they will be asked again to choose another number and so on until they win or until their eight attempts are done.\



# for i in range(1,9):
#  question != 26
#   print(try_again)

for i in range(8):
  print(try_again)