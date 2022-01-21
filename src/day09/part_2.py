from functools import reduce
from typing import List

from src.day09.helpers import find_low_points_coords
from src.global_helpers import read_input, read_int_surface
from src.global_models import Point, Surface


def calc_basin_area(visited_surface: Surface, surface: Surface, coords: Point):
    basin_area = 0
    if surface[coords] != 9 and visited_surface[coords] == 0:
        basin_area += 1
        visited_surface[coords] = 1
        for neighbour_coords in surface.square_neighbours(coords):
            basin_area += calc_basin_area(visited_surface, surface, neighbour_coords)

    return basin_area


def main():
    lines = read_input(9, 1)

    surface = read_int_surface(lines)

    low_points_coords = find_low_points_coords(surface)

    basin_areas: List[int] = [0] * len(low_points_coords)

    non_visited_rows = [[0] * surface.maxX() for _ in surface.rows]
    visited_surface = Surface(non_visited_rows)

    for i in range(len(low_points_coords)):
        basin_areas[i] = calc_basin_area(visited_surface, surface, low_points_coords[i])

    basin_areas.sort(reverse=True)
    return reduce((lambda acc, v: acc * v), basin_areas[0:3])


if __name__ == "__main__":
    print(main())
