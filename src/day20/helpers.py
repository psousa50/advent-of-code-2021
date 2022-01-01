from typing import List

from src.global_helpers import read_char_surface
from src.global_models import Point, Surface


def all_neighbours(image: Surface, p: Point):
    n = []
    for dx, dy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        point = Point(p.x + dx, p.y + dy)
        n.append(point)
    return n


def extract_binary(row_coords, image: Surface, out_pixels_are_on: bool):
    bytes = []
    for c in row_coords:
        b = "0"
        if image.is_valid_coord(c):
            b = "1" if image[c] == "#" else "0"
        else:
            b = "1" if out_pixels_are_on else "0"
        bytes += b

    return "".join(bytes).ljust(3, "0")


def enhance_image(image: Surface, algorithm: str, out_pixels_are_on: bool):
    new_rows = [["."] * (image.maxX() + 2) for _ in range(0, len(image.rows) + 2)]
    enhanced_image = Surface(new_rows)

    for y in range(-1, image.maxY() + 1):
        for x in range(-1, image.maxX() + 1):
            p = Point(x, y)
            neighbours = all_neighbours(image, p)
            r1 = extract_binary(neighbours[0:3], image, out_pixels_are_on)
            r2 = extract_binary(neighbours[3:6], image, out_pixels_are_on)
            r3 = extract_binary(neighbours[6:9], image, out_pixels_are_on)
            binary_value = r1 + r2 + r3
            value = int(binary_value, 2)
            enhanced_image[Point(x + 1, y + 1)] = algorithm[value]

    return enhanced_image


def enhance_multiple(lines: List[str], count: int):
    algorithm = lines[0]

    image = read_char_surface(lines[2:])

    for n in range(count):
        image = enhance_image(image, algorithm, out_pixels_are_on=(n % 2) == 1 and algorithm[0] == "#")

    light_count = len([c for c in image.points() if c == "#"])

    return light_count
