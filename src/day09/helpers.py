from typing import List

from src.global_models import Point, Surface

def find_low_points_coords(surface: Surface):
  low_points_coords: List[Point] = []
  for coords in surface.points_coords():
    if all([surface[coords] < surface[neighbour_coords] for neighbour_coords in surface.square_neighbours(coords)]): low_points_coords.append(coords)

  return low_points_coords
