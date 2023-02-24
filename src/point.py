import math
import random

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print_point(self):
        print(f"({self.x}, {self.y}, {self.z})")

# def distance(p: Point, q: Point) -> float:
#     return p.euclideanDistance(q)

def n_distance(p: Point, q: Point, n: int) -> float:
    return p.n_distance(q, n)

def get_n_coord(p: Point, n: int) -> float:
    return p.coords[n]

class Points:
    def __init__(self, points: list):
        self.points = points
        self.size = len(self.points)

    def add_point(self, point: Point):
        self.points.append(point)
        self.size += 1
    
    def print_points(self):
        for i in range(self.size):
            print(f"{i+1}." , end = " ")
            self.points[i].print_point()

def generate_points(n: int, dimension: int, lim: int = 100) -> Points:
    part = lim // n
    below = -lim
    above = below + part
    points = Points([])
    for _ in range(n):
        coords = []
        for _ in range(dimension):
            coords.append(random.randint(below, above))
        below = above
        above = below + part
        points.add_point(Point(*coords))

    return points

def genereate_points(n):
  points = []
  for i in range(n):
    points.append(Point(random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)))
  return points

def print_points(Points):
  for i in range (len(Points)):
    print(f"{i+1}.", end = " ")
    Points[i].print_point()

