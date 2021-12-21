from src.global_helpers import read_input

def main():
  lines = read_input(2, 1)

  commands = tuple((v[0], int(v[1])) for v in (v.split() for v in lines))

  position, depth, aim = (0, 0, 0)

  for command, units in commands:
      match(command):
          case 'forward': 
            position += units
            depth += aim * units
          case 'down': 
            aim += units
          case 'up': 
            aim -= units

  return position * depth

print(main())
