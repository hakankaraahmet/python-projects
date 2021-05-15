def perfect(number):     #Perfect Number in a limit
   perfect_list = []
   for i in range(1,number):
     if number % i == 0:
       perfect_list.append(i)
   sum_of_divisor = sum(perfect_list)      
   return sum_of_divisor == number  

for i in range(1,1000):
  if perfect(i):
    print(i) 