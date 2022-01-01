from typing import List

from src.day09.helpers import find_low_points_coords
from src.global_helpers import read_input, read_int_surface


def main():
  lines = read_input(9, 1)

  surface = read_int_surface(lines)

  low_points_coords = find_low_points_coords(surface)

  low_points = [surface[c] for c in low_points_coords]

  return sum([v + 1 for v in low_points])

print(main())
