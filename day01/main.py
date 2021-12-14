import helpers

lines = helpers.read_input(1)

values = [int(line) for line in lines]

increases = 0
for i, v in enumerate(values):
    if i > 0 and values[i] > values[i-1]:
        increases += 1

print(increases)
