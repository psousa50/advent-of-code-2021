import heapq
import sys
from collections import defaultdict, deque, namedtuple
from typing import List

from src.global_helpers import read_input
from src.global_models import Point

infinity = sys.maxsize

def get_cost(lines: List[str], p: Point):
  return int(lines[p.y][p.x])

def neighbours(point: Point, maxX, maxY):
    n = []
    for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
      (x,y) = (point.x + dx, point.y + dy)
      if x >= 0 and x < maxX and y >= 0 and y < maxY: n.append(Point(x,y))
    return n

def main():

  lines = read_input(15, 1)

  maxX = len(lines[0])
  maxY = len(lines)

  start_pos = Point(0,0)
  end_pos = Point(maxX - 1, maxY - 1)

  nodes = [(0, start_pos)]
  costs = defaultdict(lambda: infinity)
  costs[start_pos] = 0

  solutions = []
  while nodes:
    cost, point = heapq.heappop(nodes)
    if point == end_pos:
      solutions.append(cost)
    elif cost <= costs[point]:
      for neighbour in neighbours(point, maxX, maxY):
        new_cost = cost + get_cost(lines, neighbour)
        if new_cost < costs[neighbour]:
          costs[neighbour] = new_cost
          heapq.heappush(nodes, (new_cost, neighbour))

  return min(solutions)

print(main())
