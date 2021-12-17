from typing import List
import global_helpers

from src.day07.helpers import calc_minimum_fuel_cost

def calc_cost(p1, p2):
  return abs(p1 - p2) 

def main():
  lines = global_helpers.read_input(7, 1)

  positions: List[int] = [int(n) for n in lines[0].split(",")]

  fuel_cost = calc_minimum_fuel_cost(positions, calc_cost)

  return fuel_cost

print(main())


