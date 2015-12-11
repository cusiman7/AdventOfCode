#!/usr/bin/python
def run():
  import re
  input = open('day8.txt', 'r')
  
  code = 0
  data = 0
  encoded = 0
  for line in input.readlines():
    line = line[:-1] # Strip newlines
    code += len(line)
    line_data = re.sub('^"|"$','', line)
    line_data = re.sub(r'\\\\|\\"|\\x[a-f0-9]{2}','#', line_data)
    data += len(line_data)

    line_encoded = re.sub(r'\\',r'\\\\', line)
    line_encoded = re.sub('"','\\"', line_encoded)
    encoded += len(line_encoded) + 2 # 2 for start and end quotes

  print("8.a {}".format(code - data))
  print("8.b {}".format(encoded - code))
  input.close()

if __name__ == '__main__':
  run() 
