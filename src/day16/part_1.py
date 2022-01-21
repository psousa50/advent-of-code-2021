from collections import namedtuple
from typing import List

from src.day16.helpers import Packet, read_binary_packet, parse_packet
from src.global_helpers import read_input


def sum_versions(packets: List[Packet]):
    s = 0
    for p in packets:
        s += p.version + sum_versions(p.sub_packets)
    return s


def main():
    lines = read_input(16, 1)

    binary_packet = read_binary_packet(lines)

    root_packet, _ = parse_packet(binary_packet, 0)

    return sum_versions([root_packet])


if __name__ == "__main__":
    print(main())
