import sys
from dataclasses import dataclass, field
from typing import List

from src.global_helpers import read_input
from src.global_models import infinity


@dataclass(frozen=True)
class Beacon:
  x: int
  y: int
  z: int

  def __repr__(self):
    return f'{self.x}, {self.y}, {self.z}'

@dataclass()
class Scanner:
  name: str
  beacons: List[Beacon] = field(default_factory=list)
  min_x: int = infinity
  min_y: int = infinity
  min_z: int = infinity

  def __repr__(self):
    b ="\n".join([str(b) for b in self.beacons])
    return "\n".join([self.name, b, f'min: {self.min_x}, {self.min_y}, {self.min_z}', " "])

  def add_beacon(self, beacon: Beacon):
    self.beacons.append(beacon)
    self.min_x = min(self.min_x, beacon.x)
    self.min_y = min(self.min_y, beacon.y)
    self.min_z = min(self.min_z, beacon.z)

  def translate_beacons(self):
    self.beacons = [Beacon(b.x - self.min_x, b.y - self.min_y, b.z - self.min_z) for b in self.beacons]
    

def main():
  lines = read_input(19, 2, True)

  scanners: List[Scanner] = []
  for line in lines:
    if not line: continue
    if line.startswith("--- scanner"):
      scanner = Scanner(line.strip().split()[2])
      scanners.append(scanner)
      continue
    values = line.strip().split(",")
    [x, y, z] = map(int, values)
    scanner.add_beacon(Beacon(x, y, z))

  for s in scanners:
    s.translate_beacons()

  return scanners

print(main())
