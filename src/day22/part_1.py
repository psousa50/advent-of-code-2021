import re
from collections import deque, defaultdict
from dataclasses import dataclass

from src.global_helpers import read_input

Point3D = tuple[int, int, int]
Segment = tuple[int, int]


@dataclass
class Step:
    on: bool
    segments: list[Segment]


def is_within_50(s: Segment):
    return s[0] >= -50 and s[0] <= 50 and s[1] >= -50 and s[1] <= 50


def range_limited_to_50(segment: Segment):
    return range(segment[0], segment[1] + 1) if is_within_50(segment) else range(0, -1)


def points(segments: list[Segment]):
    for x in range_limited_to_50(segments[0]):
        for y in range_limited_to_50(segments[1]):
            for z in range_limited_to_50(segments[2]):
                yield (x, y, z)


def apply_steps(segments_on: set[Point3D], steps: list[Step]):
    for step in steps:
        for p in points(step.segments):
            if step.on:
                segments_on.add(p)
            else:
                segments_on.remove(p)


def segment_len(s: Segment):
    return abs(s[1] - s[0] + 1)


def read_segment(r: re.Match[str], index: int):
    return int(r.group(index)), int(r.group(index + 1))


def main():

    lines = read_input(22, 1)

    rg_number = "([x|y|z])=(-?\d+)..(-?\d+)"
    steps_rg = f"(on|off) {rg_number},{rg_number},{rg_number}"

    steps: list[Step] = []

    for line in lines:
        r = re.search(steps_rg, line)
        steps.append(Step(r.group(1) == "on", [read_segment(r, 3), read_segment(r, 6), read_segment(r, 9)]))

    segments_on: set[Point3D] = set()
    for step in steps:
        for p in points(step.segments):
            if step.on:
                segments_on.add(p)
            else:
                segments_on.discard(p)

    return len(segments_on)


print(main())
