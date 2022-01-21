from src.global_helpers import read_input

def main():
  lines = read_input(2, 1)

  commands = tuple((v[0], int(v[1])) for v in (v.split() for v in lines))

  position, depth = (0, 0)

  for command, units in commands:
      match(command):
          case 'forward': position += units
          case 'down': depth += units
          case 'up': depth -= units

  return position * depth

if __name__ == "__main__":
    print(main())
