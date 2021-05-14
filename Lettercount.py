sentence = input("Please Enter a sentence")
dictionary = dict()
for i in sentence:
  if i in dictionary.keys():
    dictionary[i] += 1
  else:
    dictionary[i] = 1

print(dictionary) 