def ebob(num1,num2):
  liste1 = []
  liste2 = []
  for i in range(2,num1+1):
    if num1 % i == 0:
      liste1.append(i)
      set_liste1 = set(liste1)
  for i in range(2,num2+1):
    if num2 % i == 0:
      liste2.append(i) 
      set_liste2 = set(liste2)  
  intersections = set_liste1.intersection(set_liste2)
  return (max(intersections))