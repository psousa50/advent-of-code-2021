from typing import List

from src.day12.models import Node


def find_solutions(paths, node: Node):
  if node.cave == 'end': return [node]

  caves: List[str] = [e for s, e in paths if s == node.cave] + [s for s, e in paths if e == node.cave and s != 'start']
  children: List[Node] = []
  for c in caves:
    revisiting_small_cave = c.islower() and c in node.path
    if not revisiting_small_cave or revisiting_small_cave and node.visits_for_small_cave < node.max_visits_for_small_cave:
      children_node = Node(c, node) 
      if revisiting_small_cave: children_node.visits_for_small_cave += 1
      children.append(children_node)

  solutions = []
  for c in children:
    solutions += find_solutions(paths, c)
  
  return solutions

