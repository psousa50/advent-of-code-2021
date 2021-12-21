from typing import NamedTuple
class Point(NamedTuple):
  x: int
  y: int

  def __repr__(self):
    return f'({self.x},{self.y})'

