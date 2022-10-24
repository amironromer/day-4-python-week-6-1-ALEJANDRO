from random import randint

def our_code():
  num=randint(0,100)
  name= input("what is your name? ")
  numOfTries = 0
  
  while True:
    question= int(input("Well {}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is? ".format(name)))
  
    if question<1 or question>100:
      print("{} has chosen a number that is out of play".format(name))
      numOfTries += 1
      print(f"Attempt: {numOfTries}")

    if question<num:
      print("The answer is wrong, {} has chose a lower number than the secret number".format(name))
      numOfTries += 1
      print(f"Attempt: {numOfTries}")

    if question>num:
      print("The answer is wrong, {} has chose a greater number than the secret number".format(name))
      numOfTries += 1
      print(f"Attempt: {numOfTries}")

    if question == num:
      print("You chose the right number, you win!")
      print(f"Your attempts: {numOfTries}")
      break

    elif numOfTries == 8:
      print("Sorry, you ran out of tries!")
      break

