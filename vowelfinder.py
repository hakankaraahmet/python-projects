def vowels(text):
  my_list1 = []
  vowellist = ["a","e","i","o","u"]
  for i in text:
    for j in vowellist:
      if i == j:
        my_list1.append(i)
  return(my_list1) 