kac = int(input("kaç defa girmek istersiniz?"))  
listem = []
for i in range(kac):
  listem.append(int(input("sayıları girin")))
  listem.sort()
if len(listem) % 2 == 0:
  print(listem[kac//2],listem[(kac//2)-1])
else:
  print(listem[kac//2])