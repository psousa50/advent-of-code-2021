from typing import List

from src.global_helpers import read_char_surface
from src.global_models import Point, Surface


def all_neighbours(image: Surface, p: Point):
    return [
        Point(p.x + dx, p.y + dy)
        for dx, dy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    ]


def enhance_image(image: Surface, algorithm: str, out_pixels_are_on: bool):
    new_rows = [["."] * (image.maxX() + 2) for _ in range(0, len(image.rows) + 2)]
    enhanced_image = Surface(new_rows)

    for y in range(-1, image.maxY() + 1):
        for x in range(-1, image.maxX() + 1):
            p = Point(x, y)
            value = 0
            for c in all_neighbours(image, p):
                valid = image.is_valid_coord(c)
                bit = 1 if valid and image[c] == "#" or not valid and out_pixels_are_on else 0
                value = 2 * value + bit
            enhanced_image[Point(x + 1, y + 1)] = algorithm[value]

    return enhanced_image


def enhance_multiple(lines: List[str], count: int):
    algorithm = lines[0]

    image = read_char_surface(lines[2:])

    for n in range(count):
        image = enhance_image(image, algorithm, out_pixels_are_on=(n % 2) == 1 and algorithm[0] == "#")

    light_count = len([c for c in image.points() if c == "#"])

    return light_count
