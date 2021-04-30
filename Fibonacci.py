result = [1]  #FIBONACCI NUMBER
a=0
b=1
for i in range(9):
  c = a+b
  result.append(c)
  a=b
  b=c
print(result)
