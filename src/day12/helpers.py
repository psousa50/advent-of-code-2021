from collections import defaultdict, deque

def read_paths(lines):
  paths = defaultdict(list)
  for line in lines:
    p = line.split("-")
    if (p[1]) != 'start': paths[p[0]].append(p[1])
    if (p[0]) != 'start': paths[p[1]].append(p[0])

  return paths

def find_solutions(paths, max_small_visits):
  start = ('start', ['start'], 0)
  nodes = deque([start])
  solutions = []
  while nodes:
    pos, path, small_visits = nodes.popleft()
    if pos == 'end':
      solutions.append(path)
    else:
      for dest in paths[pos]:
        if dest.isupper() or dest not in path:
          nodes.append((dest, path + [dest], small_visits))
        else:
          if (small_visits < max_small_visits):
            nodes.append((dest, path + [dest], small_visits + 1))

  return solutions    