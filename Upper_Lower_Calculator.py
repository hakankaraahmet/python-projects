def calculater(word):     # Upper and Lower letter Calculator
  upper_list = []
  lower_list = []
  for i in a:
    if i.isupper():
      upper_list.append(i)  
    elif i.islower():
      lower_list.append(i)
    else:
      continue  
  print(len(upper_list))
  print(len(lower_list))  