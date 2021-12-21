import math
from typing import List

from src.global_models import Surface


def read_input(day, part, sample=False):
    filename = "input" if not sample else "sample"
    filepath = f'src/day{day:02d}/inputs/{filename}_{part:02d}.txt'
    with open(filepath, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

sign = lambda x: 0 if x == 0 else int(math.copysign(1, int(x)))

def read_surface(lines: List[str]):
  rows = [[int(c) for c in line] for line in lines]
  return Surface(rows)

