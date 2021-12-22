from src.global_helpers import read_input
from src.day12.models import Node
from src.day12.helpers import find_solutions

def main():
  lines = read_input(12, 1)

  paths = [tuple(line.split("-")) for line in lines]

  solutions = find_solutions(paths, Node('start', None, 1))

  return len(solutions)

print(main())
