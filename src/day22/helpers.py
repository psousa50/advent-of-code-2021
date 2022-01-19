import re

from src.day22.models import Cube, Point3D, subtract, Step


def apply_steps(steps: list[Step]):
    cubes: list[Cube] = []
    for step in steps:
        cubes = [part for cube in cubes for part in subtract(cube, step.cube)]
        if step.on:
            cubes.append(step.cube)

    return cubes


def read_steps(lines: list[str]):
    rg_number = "([x|y|z])=(-?\d+)..(-?\d+)"
    steps_rg = f"(on|off) {rg_number},{rg_number},{rg_number}"

    steps: list[Step] = []

    for line in lines:
        r = re.search(steps_rg, line)
        if r is not None:
            is_on = r.group(1) == "on"
            cube = Cube(
                Point3D(int(r.group(3)), int(r.group(6)), int(r.group(9))),
                Point3D(int(r.group(4)), int(r.group(7)), int(r.group(10))),
            )
            steps.append(Step(is_on, cube))

    return steps
