from typing import Dict, List
from day05.helpers import count_points_usage, read_segments
import global_helpers

def main():
  lines = global_helpers.read_input(5, 1)

  segments = read_segments(lines)

  points = count_points_usage(segments)

  return len([p for p in points.values() if p > 1])

print(main())
