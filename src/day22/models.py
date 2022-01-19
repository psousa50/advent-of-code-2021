from dataclasses import dataclass


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int


@dataclass(frozen=True)
class Segment:
    start: int
    end: int

    def length(self):
        return self.end - self.start + 1

    def points(self):
        return range(self.start, self.end + 1)

    def intersects(self, other: "Segment"):
        return other.end >= self.start and other.start <= self.end


@dataclass(frozen=True)
class Cube:
    p0: Point3D
    p1: Point3D

    @classmethod
    def from_segments(cls, x_segment: Segment, y_segment: Segment, z_segment: Segment):
        return cls(
            Point3D(x_segment.start, y_segment.start, z_segment.start),
            Point3D(x_segment.end, y_segment.end, z_segment.end),
        )

    def x_segment(self):
        return Segment(self.p0.x, self.p1.x)

    def y_segment(self):
        return Segment(self.p0.y, self.p1.y)

    def z_segment(self):
        return Segment(self.p0.z, self.p1.z)

    def size(self):
        return self.x_segment().length() * self.y_segment().length() * self.z_segment().length()

    def size_trunc_50(self):
        def l(segment: Segment):
            s = max(-50, segment.start)
            e = min(50, segment.end)
            return (e - s + 1) if s <= e else 0

        return l(self.x_segment()) * l(self.y_segment()) * l(self.z_segment())


def subtract(c1: Cube, c2: Cube):
    if not intersect(c1, c2):
        return [c1]

    results = []

    if c1.p0.x <= c2.p1.x <= c1.p1.x:
        results += [Cube(Point3D(c2.p1.x + 1, c1.p0.y, c1.p0.z), Point3D(c1.p1.x, c1.p1.y, c1.p1.z))]
        c1 = Cube(Point3D(c1.p0.x, c1.p0.y, c1.p0.z), Point3D(c2.p1.x, c1.p1.y, c1.p1.z))

    if c1.p0.x <= c2.p0.x <= c1.p1.x:
        results += [Cube(Point3D(c1.p0.x, c1.p0.y, c1.p0.z), Point3D(c2.p0.x - 1, c1.p1.y, c1.p1.z))]
        c1 = Cube(Point3D(c2.p0.x, c1.p0.y, c1.p0.z), Point3D(c1.p1.x, c1.p1.y, c1.p1.z))

    if c1.p0.y <= c2.p1.y <= c1.p1.y:
        results += [Cube(Point3D(c1.p0.x, c2.p1.y + 1, c1.p0.z), Point3D(c1.p1.x, c1.p1.y, c1.p1.z))]
        c1 = Cube(Point3D(c1.p0.x, c1.p0.y, c1.p0.z), Point3D(c1.p1.x, c2.p1.y, c1.p1.z))

    if c1.p0.y <= c2.p0.y <= c1.p1.y:
        results += [Cube(Point3D(c1.p0.x, c1.p0.y, c1.p0.z), Point3D(c1.p1.x, c2.p0.y - 1, c1.p1.z))]
        c1 = Cube(Point3D(c1.p0.x, c2.p0.y, c1.p0.z), Point3D(c1.p1.x, c1.p1.y, c1.p1.z))

    if c1.p0.z <= c2.p1.z <= c1.p1.z:
        results += [Cube(Point3D(c1.p0.x, c1.p0.y, c2.p1.z + 1), Point3D(c1.p1.x, c1.p1.y, c1.p1.z))]
        c1 = Cube(Point3D(c1.p0.x, c1.p0.y, c1.p0.z), Point3D(c1.p1.x, c1.p1.y, c2.p1.z))

    if c1.p0.z <= c2.p0.z <= c1.p1.z:
        results += [Cube(Point3D(c1.p0.x, c1.p0.y, c1.p0.z), Point3D(c1.p1.x, c1.p1.y, c2.p0.z - 1))]
        # c1 = Cube(Point3D(c1.p0.x, c1.p0.y, c2.p0.z), Point3D(c1.p1.x, c1.p1.y, c1.p1.z))

    return results


def intersect(c1: Cube, c2: Cube):
    b1 = c1.x_segment().intersects(c2.x_segment())
    b2 = c1.y_segment().intersects(c2.y_segment())
    b3 = c1.z_segment().intersects(c2.z_segment())
    return b1 and b2 and b3


@dataclass
class Step:
    on: bool
    cube: Cube
