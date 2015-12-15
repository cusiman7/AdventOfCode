#!/usr/bin/python
def run():
  import itertools
  input = open('day15.txt', 'r')

  ingr = {}
  for line in input.readlines():
    (name, rest) = line.replace('\n', '').split(':')
    (capacity, durability, flavor, texture, calories) = rest.split(',')
    cap = int(capacity.split()[1])
    dur = int(durability.split()[1])
    flv = int(flavor.split()[1])
    tex = int(texture.split()[1])
    cal = int(calories.split()[1])
    ingr[name] = (cap, dur, flv, tex, cal)

  score = 0
  score2 = 0
  for x in itertools.combinations_with_replacement(ingr, 100):
    cap = 0
    dur = 0
    flv = 0
    tex = 0
    cal = 0
    for k, g in itertools.groupby(x):
      amt = len(list(g))
      cap += ingr[k][0] * amt
      dur += ingr[k][1] * amt
      flv += ingr[k][2] * amt
      tex += ingr[k][3] * amt
      cal += ingr[k][4] * amt
    
    if cap < 0 or dur < 0 or flv < 0 or tex < 0:
      continue

    score = max(score, cap * dur * flv * tex)
  
    if cal != 500:
      continue

    score2 = max(score2, cap * dur * flv * tex)

  print("15.a {}".format(score))
  print("15.b {}".format(score2))
  input.close()

if __name__ == '__main__':
  run() 
