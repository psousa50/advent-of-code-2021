import re
from typing import List, Set

from src.global_models import Point


def read_dots_and_folds(lines):
  fold_regex = "fold along ([x,y])=(\d*)"

  reading_dots = True
  dots: Set[Point] = set()
  folds = []
  for line in lines:
    if (len(line) == 0):
      reading_dots = False
      continue

    if reading_dots:
      c = line.split(",")
      dots.add(Point(int(c[0]), int(c[1])))
    else:
      r = re.search(fold_regex, line)
      folds.append((r.group(1), int(r.group(2))))

  return dots, folds