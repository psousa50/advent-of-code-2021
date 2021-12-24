import heapq
import sys
from collections import defaultdict

from src.global_models import Point

infinity = sys.maxsize

def neighbours(maxX, maxY):

  def neighbours_internal(point: Point):
    n = []
    for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
      (x,y) = (point.x + dx, point.y + dy)
      if x >= 0 and x < maxX and y >= 0 and y < maxY: n.append(Point(x,y))
    return n

  return neighbours_internal

def calc_costs(lines, end_pos, get_cost, get_neighbours):

  path_costs = []

  start_pos = Point(0,0)

  nodes = [(0, start_pos)]
  costs = defaultdict(lambda: infinity)
  costs[start_pos] = 0

  while nodes:
    cost, point = heapq.heappop(nodes)
    if point == end_pos:
      path_costs.append(cost)
    elif cost <= costs[point]:
      for neighbour in get_neighbours(point):
        new_cost = cost + get_cost(lines, neighbour)
        if new_cost < costs[neighbour]:
          costs[neighbour] = new_cost
          heapq.heappush(nodes, (new_cost, neighbour))

  return path_costs
