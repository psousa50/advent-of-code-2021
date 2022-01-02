from dataclasses import dataclass

from src.global_helpers import read_input


@dataclass
class Player:
    pos: int
    score: int = 0


@dataclass
class Dice:
    current: int = 1

    def roll3(self):
        sum = 3 * (self.current + 1)
        self.current += 3
        return sum


def main():
    lines = read_input(21, 1)

    players = [Player(int(line.split(" ")[4])) for line in lines]
    dice = Dice()

    p = 0
    while players[0].score < 1000 and players[1].score < 1000:
        dice_value = dice.roll3()
        players[p].pos = (players[p].pos + dice_value - 1) % 10 + 1
        players[p].score += players[p].pos
        p = (p + 1) % 2

    return min(p.score for p in players) * (dice.current - 1)


print(main())
