number = input("please enter a positive number:  ")
sum = 0
if int(number) > 0:
  for i in number:
   sum = sum + int(i)**len(number)
  if sum == int(number):
    print("your number is armstrong number")    
  else:
    print("your number is not armstrong")
else:
  print("invalid number")