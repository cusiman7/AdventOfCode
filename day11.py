#!/usr/bin/python
def run():
  import string
  input = 'cqjxjnds'
  alpha = string.lowercase
  def checkPass(check):
    pairCount = 0
    for c in alpha:
      if c*2 in check:
        pairCount += 1
      if pairCount >= 2:
        break

    if pairCount < 2:
      return False
  
    straight = False
    for i, c in enumerate(alpha):
      if c == 'y':
        break
      if alpha[i:i+3] in check:
        return True

    return False

  ordz = ord('z')
  def increment(s):
    i = len(s) - 1
    while i > 0:
      c = ord(s[i]) + 1
      if chr(c) in {'i', 'o', 'l'}:
        c += 1
      if c == ordz + 1:
        s = s[:i] + 'a' + s[i+1:]
        i -= 1 
      else:
        s = s[:i] + chr(c) + s[i+1:]
        break
    return s

  while not checkPass(input):
    input = increment(input)

  print("11.a {}".format(input))
  input = increment(input)
  
  while not checkPass(input):
    input = increment(input)

  print("11.b {}".format(input))

if __name__ == '__main__':
  run() 
