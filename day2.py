#!/usr/bin/python 
def run():
  input = open('day2.txt', 'r')

  sa = 0
  ribbon = 0
  for line in input.readlines():
    whl = line.split('x')
    w = int(whl[0])
    h = int(whl[1])
    l = int(whl[2])
    
    sa = sa + 2*w*h + 2*w*l + 2*h*l
    sa = sa + min(w*h, w*l, h*l)
    
    whf = 2*w + 2*h
    wlf = 2*w + 2*l
    hlf = 2*h + 2*l
    minFace = min(whf, wlf, hlf)
    v = w*h*l
    ribbon = ribbon + minFace + v
  print('2.a {}'.format(sa))
  print('2.b {}'.format(ribbon))
  input.close()

if __name__ == '__main__':
  run() 
