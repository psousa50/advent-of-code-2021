import sys
import math
import re

from src.global_helpers import read_input
from src.global_helpers import sign

minus_infinity = -sys.maxsize - 1

target_regex = "x=(-?\d*)..(-?\d*), y=(-?\d*)..(-?\d*)"


def calc_start_for(v):
  a = math.sqrt(1 + 8 * v)
  r1 = (-1 + a) / 2
  r2 = (-1 - a) / 2
  r = r1 if r1 > 0 else r2
  return r

def calc_highest_y(x_velocity, y_velocity, start_x, end_x, start_y, end_y):
  x, y = (0, 0)
  on_target = False
  passed_target = False
  highest_y = minus_infinity
  while not on_target and not passed_target:
    new_x = x + x_velocity
    new_y = y + y_velocity
    on_target = new_x >= start_x and new_x <= end_x and new_y <= end_y and new_y >= start_y

    passed_target = not on_target and (
       x_velocity > 0 and new_x > end_x or \
      x_velocity < 0 and new_x < end_x or \
      y > end_y and new_y < start_y)

    passed_target = passed_target or (x_velocity == 0 and (start_x > 0 and x < start_x or start_x < 0 and x < start_x))
    if not passed_target:
      x_velocity -= sign(x_velocity)
      y_velocity -= 1
      x = new_x
      y = new_y
      if y > highest_y: highest_y = y
  
  return on_target, highest_y

def main():
  lines = read_input(17, 1, True)

  r = re.search(target_regex, lines[0])

  start_x = int(r.group(1))
  end_x = int(r.group(2))
  start_y = int(r.group(3))
  end_y = int(r.group(4))

  min_x = math.ceil(calc_start_for(start_x))

  highest_y = minus_infinity
  x_velocity = min_x
  target_x_velocity = 0
  target_y_velocity = 0
  while x_velocity < end_x:
    y_velocity = 1
    while y_velocity < abs(start_y):
      on_target, new_highest_y = calc_highest_y(x_velocity, y_velocity, start_x, end_x, start_y, end_y)
      if on_target:
        if new_highest_y > highest_y: 
          highest_y = new_highest_y
          target_x_velocity, target_y_velocity = (x_velocity, y_velocity)
      y_velocity += 1
    x_velocity += 1

  return highest_y

print(main())
