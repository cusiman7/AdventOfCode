def run():
  input = '1113222113'
  #Finished #158

  for i in range(50):
    next = ''
    sameCount = 0
    currentChar = None
    for c in input:
      if currentChar != c and currentChar != None:
        next += str(sameCount) + currentChar
        sameCount = 0
      currentChar = c
      sameCount += 1

    next += str(sameCount) + currentChar
    input = next
    if (i == 39):
      print("10.a {}".format(len(next)))

  print("10.b {}".format(len(next)))
