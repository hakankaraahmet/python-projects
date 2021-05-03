number = []
prime = int(input("kaça kadar sayılar kontrol edilsin? "))
for i in range(2,prime):
    for k in range(2,i):
      if (i % k) == 0:
        break
    else:
       number.append(i)    
    
print(number)      
