from dataclasses import dataclass
from typing import List, NamedTuple

class Point(NamedTuple):
  x: int
  y: int

  def __repr__(self):
    return f'({self.x},{self.y})'

@dataclass
class Surface:
  square_neighbours_coords = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
  diagonal_neighbours_coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

  rows: List[List[int]]

  def __repr__(self):
    return "\n".join([f'{r}' for r in self.rows])

  def __getitem__(self, coords: Point):
    return self.rows[coords.y][coords.x]

  def __setitem__(self, coords: Point, value):
    self.rows[coords.y][coords.x] = value

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

  def square_neighbours(self, p: Point):
    return self.neighbours(p, Surface.square_neighbours_coords)

  def diagonal_neighbours(self, p: Point):
    return self.neighbours(p, Surface.diagonal_neighbours_coords)

  def neighbours(self, p: Point, neighbours_coords):
    n = []
    for dx, dy in neighbours_coords:
      point = Point(p.x + dx, p.y + dy)
      if self.is_valid_coord(point): n.append(point)
    return n

