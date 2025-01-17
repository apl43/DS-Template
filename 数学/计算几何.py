from math import sqrt


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y
    # 加
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    # 减
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    # 乘 (必须写成 Point * num)
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)
    def __repr__(self):
        return f"{self.x, self.y}"

Vector = Point    
# 获取向量
def get_vec(p1: Point, p2: Point) -> Vector:
    return Vector(p2.x - p1.x, p2.y - p1.y)

# 点乘
def dot_product(v1: Vector, v2: Vector) -> float:
    return v1.x * v2.x + v1.y * v2.y

# 叉乘
def cross_product(v1: Vector, v2: Vector) -> Vector:
    return v1.x * v2.y - v1.y * v2.x

# 两点距离
def distance(p1: Point, p2: Point) -> float:
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# p1 到 p2p3 距离
def point2line_distance(p1: Point, p2: Point, p3: Point) -> float:
    cross = cross_product(get_vec(p1, p2), get_vec(p1, p3))
    return abs(cross) / distance(p2, p3)

# 三点确定一个圆心
def center_of_the_circle(p1: Point, p2: Point, p3: Point) -> Point:
    a, b = p1.x - p2.x, p1.y - p2.y
    c, d = p1.x - p3.x, p1.y - p3.y
    e = (p1.x ** 2 - p2.x ** 2 + p1.y ** 2 - p2.y ** 2) / 2
    f = (p1.x ** 2 - p3.x ** 2 + p1.y ** 2 - p3.y ** 2) / 2
    # 三点共线无圆心
    if b * c == a * d:
        return None
    x = (b * f - d * e) / (b * c - a * d)
    y = (c * e - a * f) / (b * c - a * d)
    return Point(x, y)