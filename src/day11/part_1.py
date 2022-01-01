from src.global_helpers import read_input, read_int_surface
from src.day11.helpers import increase_level

def main():
  lines = read_input(11, 1)

  surface = read_int_surface(lines)

  flashes = 0
  for _ in range(100):
    flashes += increase_level(surface, surface.points_coords())

    for c in surface.points_coords():
      if surface[c] > 9: surface[c] = 0
  
  return flashes

print(main())