from typing import List
from src.global_models import Point, Surface

def increase_level(surface: Surface, coords_to_increase: List[Point]):
  to_flash: List[Point] = []
  for c in coords_to_increase:
    surface[c] += 1
    if surface[c] == 10: to_flash.append(c)

  flashes = len(to_flash)

  for f in to_flash:
    flashes += increase_level(surface, surface.diagonal_neighbours(f))    

  return flashes

