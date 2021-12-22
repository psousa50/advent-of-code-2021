from src.global_helpers import read_input
from src.day12.models import Node

def find(paths, node: Node):
  if node.cave == 'end': return [node]

  caves = [e for s, e in paths if s == node.cave] + [s for s, e in paths if e == node.cave and s != 'start']
  children = [Node(c, node) for c in caves if c.isupper() or c not in node.path]
  solutions = []
  for c in children:
    solutions += find(paths, c)
  
  return solutions

def main():
  lines = read_input(12, 1)

  paths = [tuple(line.split("-")) for line in lines]

  solutions = find(paths, Node('start'))

  return len(solutions)

print(main())
