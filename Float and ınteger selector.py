def secici(lists):
    floats = []
    integers = []
    for i in lists:
      for j in i:
        if type(j) == float:
         floats.append(j)
        else:
          integers.append(j)
    return floats,integers