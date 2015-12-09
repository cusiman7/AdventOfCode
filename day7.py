def run():
  import copy
  input = open('day7.txt', 'r')

  signals = {}
  for line in input.readlines():
    inout = line.strip('\n ').split(' -> ')
    signals[inout[1]] = inout[0]

  signals_og = copy.deepcopy(signals)

  def num(s):
    try:
      return int(s)
    except ValueError:
      return None

  def solve(s):
    if num(s) is not None: return num(s)
    if num(signals[s]) is not None: return num(signals[s])
    instr = signals[s].split(' ')
    if len(instr) == 1:
      v = solve(instr[0])
    elif len(instr) == 2:
      gate = instr[0]
      if gate == 'NOT':
        v = ~solve(instr[1])
    elif len(instr) == 3:
      gate = instr[1]
      if gate == 'AND':
        v = (solve(instr[0]) & solve(instr[2]))
      elif gate == 'OR':
        v = (solve(instr[0]) | solve(instr[2]))
      elif gate == 'LSHIFT':
        v = (solve(instr[0]) << solve(instr[2]))
      elif gate == 'RSHIFT':
        v = (solve(instr[0]) >> solve(instr[2]))
    signals[s] = v
    return v

  a1 = solve('a')

  signals = copy.deepcopy(signals_og)
  signals['b'] = a1

  a2 = solve('a')
  
  print("7.a {}".format(a1 & 0xFFFF))
  print("7.b {}".format(a2 & 0xFFFF))
  input.close()
