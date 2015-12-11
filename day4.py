#!/usr/bin/python
def run():
  import md5
  input = 'iwrupvqb'

  i = 0
  h5 = ""
  h6 = ""
  while(True):
    i = i + 1
    h = md5.new(input + str(i)).hexdigest()
    if(h5 is "" and h.startswith('0'*5)):
      h5 = h
      print("\r4.a " + str(i) + " "*32)
    if(h6 is "" and h.startswith('0'*6)):
      h6 = h
      print("\r4.b " + str(i) + " "*32)
    if(h5 is not "" and h6 is not ""):
      break
    print("\r" + h), # Because yay

if __name__ == '__main__':
  run()   
