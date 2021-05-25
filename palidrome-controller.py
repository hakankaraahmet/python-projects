def pal(sentence):
  pali = sentence.lower()
  liste = []
  for i in pali:
    if i.isalnum():
      liste.append(i)
  if liste[::-1] == liste:
    return(True)
  else:
    return(False)
print(pal("hakan"))