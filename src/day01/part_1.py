import global_helpers

def main():
  lines = global_helpers.read_input(1, 1)

  values = [int(line) for line in lines]

  increases = 0
  for i, _ in enumerate(values):
      if i > 0 and values[i] > values[i-1]:
          increases += 1

  return increases

print(main())
