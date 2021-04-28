number = int(input("Please enter a number"))  
total_even = 0
total_odd = 0
for i in range(1,number):
  if i % 2 == 0:
    total_even += i
  else:
    total_odd += i

print("Total of even number is: {}".format(total_even))
print("Total of odd number is: {}".format(total_odd))