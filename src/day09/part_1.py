from typing import List

from src.day09.helpers import find_low_points_coords, read_surface
from src.global_helpers import read_input


def main():
  lines = read_input(9, 1)

  surface = read_surface(lines)

  low_points_coords = find_low_points_coords(surface)

  low_points = [surface[c] for c in low_points_coords]

  return sum([v + 1 for v in low_points])

print(main())
