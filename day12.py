#!/usr/bin/python
def run():
  import json  
  input = open('day12.txt', 'r')
  data = json.load(input)

  def parseJSON(data, ignores=None):
    total = 0
    if type(data) is int:
      total = data
    if type(data) is dict:
      for key, value in data.iteritems():
        if value == ignores:
          return 0
        total += parseJSON(value, ignores)
    if type(data) is list:
      for value in data:
        total += parseJSON(value, ignores)
    return total

  sums = parseJSON(data)
  sums2 = parseJSON(data, u'red')

  print("12.a {}".format(sums))
  print("12.b {}".format(sums2))
  input.close()

if __name__ == '__main__':
  run() 
