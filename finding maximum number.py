counter = 0   
numberlist = []
number_size = int(input("How many numbers will you enter? "))
while counter < number_size:
  number = int(input("please enter number"))
  numberlist.append(number)
  counter = counter + 1
numberlist.sort()
print("The largest number in the list is:",numberlist[-1])