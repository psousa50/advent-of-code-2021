import helpers

def main():
  lines = helpers.read_input(1, 1)

  values = [int(line) for line in lines]

  increases = 0
  for i, _ in enumerate(values):
      if i > 2 and values[i] > values[i-3]:
          increases += 1

  return increases

print(main())
