from typing import List
from src.day09.models import Surface

from src.global_models import Point

def read_surface(lines: List[str]):
  rows = [[int(c) for c in line] for line in lines]
  return Surface(rows)

def find_low_points_coords(surface: Surface):
  low_points_coords: List[Point] = []
  for coords in surface.points_coords():
    value = surface[coords]
    if all([value < surface[n] for n in surface.neighbours(coords)]): low_points_coords.append(coords)

  return low_points_coords