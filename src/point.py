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

class Points:
    def __init__(self, *points):
        self.points = list(points)
        self.size = len(self.points)

    def add_point(self, point: Point):
        self.points.append(point)
        self.size += 1

    def remove_point(self, index: int):
        self.points.pop(index)
        self.size -= 1

    def get_point(self, index) -> Point:
        return self.points[index]

    def distance(self, i: int, j: int) -> float:
        return self.points[i].euclideanDistance(self.points[j])
    
    def print_points(self):
        for i in range(self.size):
            print(f"{i+1}." , self.points[i].coords)
    
def generate_points(n: int, dimension: int, lim: int = 100) -> Points:
    points = Points()
    part = lim // n
    below = -lim
    above = below + part
    for _ in range(n):
        coords = []
        for _ in range(dimension):
            coords.append(random.randint(below,above))
            below = above
            above = below + part
        points.add_point(Point(*coords))
    return points
