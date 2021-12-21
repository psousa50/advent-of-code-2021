from dataclasses import dataclass
from typing import NamedTuple

from src.global_helpers import sign
from src.global_models import Point
@dataclass
class Segment:
    start: Point
    end: Point

    def __repr__(self):
      return f'({self.start} => {self.end})'

    def is_vertical(self):
      return self.start.x == self.end.x

    def is_horizontal(self):
      return self.start.y == self.end.y

    def points(self):
      sx = self.end.x - self.start.x
      sy = self.end.y - self.start.y
      sign_x = sign(sx)
      sign_y = sign(sy)
      len_x = abs(sx) + 1
      len_y = abs(sy) + 1
      seg_len = max(len_x, len_y)
      x = self.start.x
      y = self.start.y
      for p in range(seg_len):
        yield Point(x, y)
        x += sign_x
        y += sign_y


