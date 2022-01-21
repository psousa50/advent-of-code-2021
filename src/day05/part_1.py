from typing import Dict, List
from src.day05.helpers import count_points_usage, read_segments
from src.global_helpers import read_input


def main():
    lines = read_input(5, 1)

    segments = read_segments(lines)

    horz_or_vert_segments = [s for s in segments if s.is_vertical() or s.is_horizontal()]
    points = count_points_usage(horz_or_vert_segments)

    return len([p for p in points.values() if p > 1])


if __name__ == "__main__":
    print(main())
