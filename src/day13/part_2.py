from typing import Set

from src.global_helpers import read_input
from src.global_models import Point, Surface
from src.day13.helpers import fold_dots, read_dots_and_folds


def main():

  lines = read_input(13, 1)

  dots, folds = read_dots_and_folds(lines)

  for fold in folds:
    dots = fold_dots(dots, fold)

  maxX = max([d.x for d in dots])
  maxY = max([d.y for d in dots])
  rows = [[' '] * (maxX + 1) for _ in range(maxY + 1)]
  surface = Surface(rows)

  for d in dots:
    surface[d] = '#'

  s = "\n".join(r for r in ["".join([c for c in row]) for row in surface.rows])

  return s

print(main())
