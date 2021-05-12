def front_back(word):
  if len(word) > 1:
    word = word[-1] + word[1:-1] + word [0]
    return word
  else:
    return word

front_back("ab")    