from collections import namedtuple
from functools import reduce
from typing import List

from src.day16.helpers import Packet, read_binary_packet, parse_packet
from src.global_helpers import read_input


def calc_packet_value(packet: Packet):
  sub_packets_values = list(map(calc_packet_value, packet.sub_packets))
  value = 0
  match(packet.type):
    case 4: value = packet.literal
    case 0: value = sum(sub_packets_values)
    case 1: value = reduce(lambda acc, v: acc * v, sub_packets_values)
    case 2: value = min(sub_packets_values)
    case 3: value = max(sub_packets_values)
    case 5: value = 1 if sub_packets_values[0] > sub_packets_values[1] else 0
    case 6: value = 1 if sub_packets_values[0] < sub_packets_values[1] else 0
    case 7: value = 1 if sub_packets_values[0] == sub_packets_values[1] else 0
  
  return value

def main():
  lines = read_input(16, 1)
  
  binary_packet = read_binary_packet(lines)

  root_packet, _ = parse_packet(binary_packet, 0)

  return calc_packet_value(root_packet)

print(main())

