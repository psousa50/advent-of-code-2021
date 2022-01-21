from src.day06.helpers import generations
from src.global_helpers import read_input


def main():
    lines = read_input(6, 1)

    lantern_fish_timers = [int(n) for n in lines[0].split(",")]

    next_lantern_fish_timers = generations(80, lantern_fish_timers)

    return sum(next_lantern_fish_timers.values())


if __name__ == "__main__":
    print(main())
