import functools
import itertools
from dataclasses import dataclass

from src.global_helpers import read_input


@functools.cache
def calc_wins(p1_pos: int, p1_score: int, p2_pos: int, p2_score: int):
    p1_wins = p2_wins = 0
    dice = (1, 2, 3)
    rolls = itertools.product(dice, dice, dice)
    for r1, r2, r3 in rolls:
        next_p1_pos = (p1_pos + r1 + r2 + r3 - 1) % 10 + 1
        next_p1_score = p1_score + next_p1_pos
        if next_p1_score >= 21:
            p1_wins += 1
        else:
            next_p2_wins, next_p1_wins = calc_wins(p2_pos, p2_score, next_p1_pos, next_p1_score)
            p1_wins += next_p1_wins
            p2_wins += next_p2_wins
    return p1_wins, p2_wins


def main():
    lines = read_input(21, 1)

    players = [int(line.split(" ")[4]) for line in lines]

    p1_wins, p2_wins = calc_wins(players[0], 0, players[1], 0)

    return max(p1_wins, p2_wins)


print(main())
