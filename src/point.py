import math
import random

class Point:
    def __init__(self, *coords: list):
        self.coords = coords
        self.dimension = len(coords)

    def euclideanDistance(self, q: 'Point') -> float:
        if self.dimension != q.dimension:
            raise ValueError("Point have different dimensions!")
        return math.sqrt(sum((self.coords[i] - q.coords[i])**2 
                             for i in range(self.dimension)))
    
    def n_distance(self, q: 'Point', n: int) -> float:
        return abs(self.coords[n] - q.coords[n])

    def print_point(self):
        print(self.coords)

def distance(p: Point, q: Point) -> float:
    return p.euclideanDistance(q)

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
