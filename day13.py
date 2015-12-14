#!/usr/bin/python
def run():
  import re
  import collections
  import itertools
  input = open('day13.txt', 'r')

  ppl = collections.defaultdict(dict)
  ppl2 = collections.defaultdict(dict)
  for line in input.readlines():
    (person1, gainlose, happiness, person2) = re.search('(\w*)\s\w*\s(\w*)\s(\d*)(?:\s\w*){6}\s(\w*)', line).group(1,2,3,4)

    if gainlose == 'gain':
      val = int(happiness)
    else:
      val = -1 * int(happiness)
    ppl[person1][person2] = val
    ppl2[person1][person2] = val
 
  ppl2['Me'] = {}
  for k in ppl2:
    ppl2[k]['Me'] = 0
    ppl2['Me'][k] = 0

  def permute(ppl):
    best = 0
    for s in itertools.permutations(ppl):
      c = len(s)
      s += (s[0],)
      total = 0
      for i in range(c):
        total += ppl[s[i]][s[i+1]] + ppl[s[i+1]][s[i]]
      best = max(best, total)
    return best

  best = permute(ppl)
  best2 = permute(ppl2)

  print("13.a {}".format(best))
  print("13.b {}".format(best2))
  input.close()

if __name__ == '__main__':
  run()
