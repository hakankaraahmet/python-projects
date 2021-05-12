 def perfect(number):     #Perfect Number
   perfect_list = []
   for i in range(1,number):
     if number % i == 0:
       perfect_list.append(i)  
   sum_of_divisor = sum(perfect_list)  
   if sum_of_divisor == number:
     print("{} is a perfect number".format(number)) 
   else:
     print("{} is not a  perfect number".format(number)) 