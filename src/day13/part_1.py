from typing import Set

from src.global_helpers import read_input
from src.global_models import Point
from src.day13.helpers import fold_dots, read_dots_and_folds


def main():

  lines = read_input(13, 1)

  dots, folds = read_dots_and_folds(lines)

  dots = fold_dots(dots, folds[0])

  return len(dots)

print(main())
