#!/usr/bin/python
def run():
  import string
  input = open('day5.txt', 'r')
  
  countA = 0
  countB = 0
  for line in input.readlines():
    #Part One
    vowels = {'a', 'e', 'i', 'o', 'u'}
    baddies = {'ab', 'cd', 'pq', 'xy'}
    vowel = (3 <= reduce(lambda x, c: x + (c in vowels), line, 0))
    double = False
    for c in string.letters:
      double = (c*2 in line)
      if double: break
    bad = False
    for baddy in baddies:
      bad = (baddy in line)
      if bad: break
    if (vowel and double and not bad): 
      countA += 1

    #Part Two
    i = 0
    pairs = False
    repeat = False
    while (i < len(line) - 2):
      pair = line[i:i+2]
      if (line.count(pair) >= 2):
        pairs = True
      if line[i] is line[i+2]:
        repeat = True
      if (pairs and repeat):
        countB += 1
        break
      i += 1

  print('5.a {}'.format(countA))
  print('5.b {}'.format(countB))
  input.close()   

if __name__ == '__main__':
  run()  
