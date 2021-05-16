def pisagor(number):
  liste = []
  for i in range(1,number):
    for j in range(1,number):
      k = (i**2 + j**2) ** 0.5
      if k == int(k):
        liste.append((i,j,k))
  return(liste) 