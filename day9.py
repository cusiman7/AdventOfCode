def run():
  import copy
  import sys
  input = open('day9.txt', 'r')
  
  class Loc:
    def __init__(self, name):
      self.name = name
      self.distances = {}

    def visit(self, visited, dist_travelled, routes):
      if len(visited) == len(self.distances) + 1:
        routes[0] = min(routes[0], dist_travelled)
        routes[1] = max(routes[1], dist_travelled)
        return
      for dest, dist in self.distances.iteritems():
        if dest not in visited:
          visited.append(dest)
          locs[dest].visit(copy.deepcopy(visited), dist_travelled + dist, routes)
          visited.pop()

  locs = {}
  for line in input.readlines():
    args = line[:-1].split(' ')
    if args[0] not in locs:
      loc = Loc(args[0])
      locs[args[0]] = loc
    if args[2] not in locs:
      loc = Loc(args[2])
      locs[args[2]] = loc
    loc = locs[args[0]]
    loc.distances[args[2]] = int(args[4])
    loc = locs[args[2]]
    loc.distances[args[0]] = int(args[4])

  routes = [sys.maxint, 0]
  for loc in locs.values():
    visited = [ loc.name ]
    loc.visit(copy.deepcopy(visited), 0, routes)
  
  print("9.a {}".format(routes[0]))
  print("9.b {}".format(routes[1]))
  input.close()
