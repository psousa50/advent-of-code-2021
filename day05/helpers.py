from typing import Dict, List
from day05.models import Point, Segment

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

def count_points_usage(segments: List[Segment]):

  points : Dict[Point, int] = {}
  for s in segments:
    for p in s.points():
      points[p] = points.get(p, 0) + 1

  return points
