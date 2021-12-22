from typing import Set

from src.global_helpers import read_input
from src.global_models import Point
from src.day13.helpers import read_dots_and_folds


def main():

  lines = read_input(13, 1)

  dots, folds = read_dots_and_folds(lines)
  
  coord, amount = folds[0]
  new_dots = set(dots)
  for d in dots:
    match coord:
      case 'x': new_dots.add(Point(2 * amount - d.x, d.y))
      case 'y': new_dots.add(Point(d.x, 2 * amount - d.y))
    new_dots.remove(d)

  return len(new_dots)

print(main())
