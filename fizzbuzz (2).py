def fibu(number):
  fizz = []
  buzz = []
  fizzbuzz = []
  unchanged = []
  for i in range(1,number):
    if i % 5 == 0 and i % 3 == 0:
      fizzbuzz.append(i)
    elif i % 5 == 0:
      buzz.append(i)
    elif i % 3 == 0:
      fizz.append(i)
    else:
      unchanged.append(i)
  print("numbers which multiple of 3:{} ".format(fizz))
  print("numbers which multiple of 5:{} ".format(buzz))
  print("numbers which multiple of both 3 and 5:{} ".format(fizzbuzz))
  print("numbers which is not multiple neither 3 or 5{} ".format(unchanged))   

fibu(100)   