#!/usr/bin/python
def run():
  import re
  input = open('day14.txt', 'r')

  class deer():
    def __init__(self, name, speed, dur, rest):
      self.name = name
      self.speed = speed
      self.dur = dur
      self.rest = rest
      self.resting = False
      self.dist = 0
      self.points = 0
      self.flycount = 0
      self.restcount = 0

    def race(self, time):
      while time > 0:
        if not self.resting:
          t = min(self.dur, time)
          time -= t
          self.flycount += t
          self.dist += self.speed * t
          if self.flycount == self.dur:
            self.resting = True
            self.flycount = 0
        else:
          t = min(self.rest, time)
          time -= t
          self.restcount += t
          if self.restcount == self.rest:
            self.resting = False
            self.restcount = 0

  reindeer = []
  for line in input.readlines():
    (name, speed, dur, rest) = re.search('(\w*)(?:\s\w*){2}\s(\d*)[a-z\/ ]*(\d*)[a-z ,]*(\d*)', line).group(1,2,3,4)
    reindeer.append(deer(name, int(speed), int(dur), int(rest)))

  for i in range(2503):
    for d in reindeer:
      d.race(1)
    windist = 0
    for d in reindeer:
      windist = max(windist, d.dist)
    for d in reindeer:
      if d.dist == windist:
        d.points += 1

  winpoints = 0
  for d in reindeer:
    winpoints = max(winpoints, d.points)

  print("14.a {}".format(windist))
  print("14.b {}".format(winpoints))
  input.close()

if __name__ == '__main__':
  run()
