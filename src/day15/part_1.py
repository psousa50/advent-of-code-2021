from typing import List

from src.day15.helpers import calc_costs, neighbours
from src.global_helpers import read_input
from src.global_models import Point


def get_cost(lines: List[str], p: Point):
    return int(lines[p.y][p.x])


def main():

    lines = read_input(15, 1)

    maxX = len(lines[0])
    maxY = len(lines)

    end_pos = Point(maxX - 1, maxY - 1)

    path_costs = calc_costs(lines, end_pos, get_cost, neighbours(maxX, maxY))

    return min(path_costs)


if __name__ == "__main__":
    print(main())
