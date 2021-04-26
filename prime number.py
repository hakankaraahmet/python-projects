number = int(input("Please enter a number: ")) 
if number > 2:
  for i in range(2,number):
    if number % i == 0:
      print("Your number is a not prime number")
      break
  else:
    print("Your number is a prime number")
elif number == 2:
  print("Your number is a prime number")      
else:
  print("Your number is not prime number")    