import random 
random = random.randint(0,5)
guesses_left = 3
while guesses_left > 0:
  guess = int(input("Please guess the number"))
  guesses_left -= 1
  if guesses_left > 0:
    if guess == random:
      print("you win")
      break
    else:
      print("try again")   
  else:
    print("still not true.no chance remain") 