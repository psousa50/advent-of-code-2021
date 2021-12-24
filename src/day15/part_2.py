from typing import List

from src.day15.helpers import calc_costs, neighbours
from src.global_helpers import read_input
from src.global_models import Point


def get_cost(maxX, maxY):

  def get_cost_internal(lines: List[str], p: Point):
    gx, x = divmod(p.x, maxX)
    gy, y = divmod(p.y, maxY)

    c = int(lines[y][x]) + gx + gy
    c = (c-1) % 9 + 1

    return c

  return get_cost_internal

def main():

  lines = read_input(15, 1)

  maxX = len(lines[0])
  maxY = len(lines)

  virtual_maxX = maxX * 5
  virtual_maxY = maxY * 5

  end_pos = Point(virtual_maxX - 1, virtual_maxY - 1)

  path_costs = calc_costs(lines, end_pos, get_cost(maxX, maxY), neighbours(virtual_maxX, virtual_maxY))

  return min(path_costs)

print(main())
