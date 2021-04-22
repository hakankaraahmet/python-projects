import random
a = random.randint(0,100)
counter = 0

while True:
  num = input("enter a number: ")
  if num == "q":
    print("quitting program")
    break
  elif int(num) > a:
    print("your number is bigger than random number")
    counter = counter +1
  elif int(num) < a:
    print("your number is smaller than random number")
    counter = counter +1
  else:
    print("Correct","trying numbers=",counter)
    break