import helpers

lines = helpers.read_input(2, 2)

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

print(position * depth)
