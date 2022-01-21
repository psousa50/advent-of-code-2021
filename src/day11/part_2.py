from src.global_helpers import read_input, read_int_surface
from src.day11.helpers import increase_level


def main():
    lines = read_input(11, 1)

    surface = read_int_surface(lines)

    step = 0
    all_flashed = False
    while not all_flashed:
        step += 1
        increase_level(surface, surface.points_coords())

        for c in surface.points_coords():
            if surface[c] > 9:
                surface[c] = 0

        all_flashed = all([surface[c] == 0 for c in surface.points_coords()])

    return step


if __name__ == "__main__":
    print(main())
