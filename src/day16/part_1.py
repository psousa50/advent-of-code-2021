from collections import namedtuple
from typing import List

from src.global_helpers import read_input

Packet = namedtuple('Packet', 'version type literal sub_packets')

def read_bits(binary_packet: List[str], pos: int, size: int):
  bits = binary_packet[pos:pos+size]
  return bits, pos + size

def read_number(binary_packet: List[str], pos: int, size: int):
  bits, pos = read_bits(binary_packet, pos, size)  
  return int(bits, 2), pos

def read_literal(binary_packet: List[str], pos: int):
  last_group = 1
  digits = ""
  while last_group == 1:
    last_group, pos = read_number(binary_packet, pos, 1)
    digit, pos = read_bits(binary_packet, pos, 4)
    digits += digit
  return int(digits, 2), pos

def read_sub_packets(binary_packet: List[str], pos: int):
  sub_packets = []
  length_type_id, pos = read_number(binary_packet, pos, 1)
  if length_type_id == 0:
    total_length, pos = read_number(binary_packet, pos, 15)
    start_pos = pos
    while pos - start_pos < total_length:
      sub_packet, pos = read_packet(binary_packet, pos)
      sub_packets.append(sub_packet)

  if length_type_id == 1:
    number_of_sub_packets, pos = read_number(binary_packet, pos, 11)
    for _ in range(number_of_sub_packets):
      sub_packet, pos = read_packet(binary_packet, pos)
      sub_packets.append(sub_packet)

  return sub_packets, pos

def read_packet(binary_packet: List[str], pos: int):
  version, pos = read_number(binary_packet, pos, 3)
  type, pos = read_number(binary_packet, pos, 3)
  literal = None
  sub_packets = []
  if type == 4:
    literal, pos = read_literal(binary_packet, pos)
  else:
    sub_packets, pos = read_sub_packets(binary_packet, pos)
  return Packet(version, type, literal, sub_packets), pos

def sum_versions(packets: List[Packet]):
  s = 0
  for p in packets:
    s += p.version + sum_versions(p.sub_packets)
  return s

def main():
  lines = read_input(16, 1)

  packet = lines[0]

  unpadded_binary_packet = bin(int(packet, 16))[2:]
  bits_len = len(unpadded_binary_packet)

  pad = int((bits_len + 3) / 4) * 4
  
  binary_packet = unpadded_binary_packet.zfill(pad)

  root_packet, pos = read_packet(binary_packet, 0)

  return sum_versions([root_packet])

print(main())
