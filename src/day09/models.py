from dataclasses import dataclass
from typing import List

from src.global_models import Point

@dataclass
class Surface:
  rows: List[Point]

  def __getitem__(self, coords: Point):
    return self.rows[coords.y][coords.x]

  def maxX(self):
    return len(self.rows[0])

  def maxY(self):
    return len(self.rows)

  def points_coords(self):
    for x in range(self.maxX()):
      for y in range(self.maxY()):
        yield Point(x, y)

  def is_valid_coord(self, p: Point):
    return p.x >= 0 and p.x < self.maxX() and p.y >= 0 and p.y < self.maxY()

  def neighbours(self, p: Point):
    n = []
    for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
      point = Point(p.x + dx, p.y + dy)
      if self.is_valid_coord(point): n.append(point)
    return n

