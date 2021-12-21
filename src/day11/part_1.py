from typing import List
from src.global_models import Point, Surface
from src.global_helpers import read_input, read_surface


def increase(surface: Surface, coords_to_increase: List[Point]):
  to_flash: List[Point] = []
  for c in coords_to_increase:
    surface[c] += 1
    if surface[c] == 10: to_flash.append(c)

  flashes = len(to_flash)

  for f in to_flash:
    flashes += increase(surface, surface.diagonal_neighbours(f))    

  return flashes

def main():
  lines = read_input(11, 1)

  surface = read_surface(lines)

  flashes = 0
  for _ in range(100):
    flashes += increase(surface, surface.points_coords())

    for c in surface.points_coords():
      if surface[c] > 9: surface[c] = 0
  
  return flashes

print(main())