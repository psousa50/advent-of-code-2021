from typing import List
from src.global_helpers import read_input

from src.day07.helpers import calc_minimum_fuel_cost

def calc_cost(p1, p2):
  d = abs(p1 - p2)
  return int (d * (d + 1) / 2)

def main():
  lines = read_input(7, 1)

  positions: List[int] = [int(n) for n in lines[0].split(",")]

  fuel_cost = calc_minimum_fuel_cost(positions, calc_cost)

  return fuel_cost

print(main())


