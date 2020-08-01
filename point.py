class Point:
    def __init__(self, x=1, y=2, z=3):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    # Bonus 1
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Point(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Point(new_x, new_y, new_z)

    # Bonus 2
    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)

    # Bonus 3
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

p1 = Point(1, 2, 3)
p2 = p1 * 2
print(p2)