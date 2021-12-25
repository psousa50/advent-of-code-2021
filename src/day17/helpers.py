import re

from src.global_helpers import sign

target_regex = "x=(-?\d*)..(-?\d*), y=(-?\d*)..(-?\d*)"

def find_solutions(lines):

  r = re.search(target_regex, lines[0])

  start_x = int(r.group(1))
  end_x = int(r.group(2))
  start_y = int(r.group(3))
  end_y = int(r.group(4))

  solutions = set()
  for y_velocity in range(start_y, abs(start_y) + 1):
    for x_velocity in range(1, end_x + 1):
      x = y = 0
      xv = x_velocity
      yv = y_velocity
      highest_y = 0
      for t in range(2 * abs(start_y) + 2):
        x += xv
        y += yv
        xv -= sign(xv)
        yv -= 1
        highest_y = max(y, highest_y)

        if start_x <= x <= end_x and start_y <= y <= end_y:
          solutions.add((x_velocity, y_velocity, highest_y))

        if x > end_x and y > end_y: break

  return solutions