import math
from typing import Dict, List, NamedTuple
from dataclasses import dataclass, field
import global_helpers

sign = lambda x: int(math.copysign(1, int(x)))

class Point(NamedTuple):
  x: int
  y: int

  def __repr__(self):
    return f'({self.x},{self.y})'

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
      signx = sign(self.end.x - self.start.x)
      signy = sign(self.end.y - self.start.y)
      for x in range(self.start.x, self.end.x + signx, signx):
        for y in range(self.start.y, self.end.y + signy, signy):
          yield Point(x, y)

def read_coord(c: str):
  points = c.split(",")
  return Point(int(points[0]), int(points[1]))

def read_segments(lines: List[str]):
  segments: List[Segment] = []
  for line in lines:
    seg = line.split("->")
    start = read_coord(seg[0])
    end = read_coord(seg[1])
    segments.append(Segment(start, end))

  return segments

def main():
  lines = global_helpers.read_input(5, 1)

  segments = read_segments(lines)

  points : Dict[Point, int] = {}
  horz_or_vert_segments = [s for s in segments if s.is_vertical() or s.is_horizontal()]
  for s in horz_or_vert_segments:
    for p in s.points():
      points[p] = points.get(p, 0) + 1

  return len([p for p in points.values() if p > 1])

print(main())
