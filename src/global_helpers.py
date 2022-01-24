import math
from time import perf_counter
from typing import List

from src.global_models import Surface


def read_input(day, part, sample=False):
    lines = read_input_raw(day, part, sample)
    return [line.strip() for line in lines]


def read_input_raw(day, part, sample=False):
    filename = "input" if not sample else "sample"
    filepath = f"src/day{day:02d}/inputs/{filename}_{part:02d}.txt"
    with open(filepath, "r", encoding="utf8") as f:
        lines = f.readlines()
    return lines


sign = lambda x: 0 if x == 0 else int(math.copysign(1, int(x)))


def read_int_surface(lines: List[str]):
    rows = [[int(c) for c in line] for line in lines]
    return Surface(rows)


def read_char_surface(lines: List[str]):
    rows = [[c for c in line] for line in lines]
    return Surface(rows)


def execute(f):
    start_time = perf_counter()
    print()
    print(f"Result: {f()}")
    print()
    total_time = perf_counter() - start_time
    print(f"Total time: {total_time:.3f} seconds")
