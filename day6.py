#!/usr/bin/python
def run():
  import re
  input = open('day6.txt', 'r')
 
  lightsA = [[0]*1000 for i in range(1000)]
  lightsB = [[0]*1000 for i in range(1000)]
  
  for line in input.readlines():
    m = re.search('([a-z]*\s[a-z]*)\D*(\d+),(\d+)\D*(\d+),(\d+)', line)
    command = m.group(1).strip()
    start = m.group(2,3)
    end = m.group(4,5)

    for col in range(int(start[0]), int(end[0]) + 1):
      for row in range(int(start[1]), int(end[1]) + 1):
        if command == 'turn on':
          lightsA[row][col] = 1
          lightsB[row][col] += 1
        if command == 'turn off':
          lightsA[row][col] = 0
          lightsB[row][col] = max(0, lightsB[row][col] - 1)
        if command == 'toggle':
          lightsA[row][col] = not lightsA[row][col]
          lightsB[row][col] += 2

  count = 0
  brightness = 0
  for col in range(1000):
    for row in range(1000):
      count += lightsA[row][col]
      brightness += lightsB[row][col]

  print("6.a {}".format(count))
  print("6.a {}".format(brightness))
  input.close()

if __name__ == '__main__':
  run() 
