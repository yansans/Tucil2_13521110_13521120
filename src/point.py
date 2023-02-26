import math
import random

class Point:
    def __init__(self, coords: list):
        self.c = coords
        self.d = len(coords)
    
    def print_point(self):
        print("(", end="")
        for i in range(self.d):
            if i == self.d - 1:
                print(f"{self.c[i]})")
            else:
                print(f"{self.c[i]}; " , end="")

def random_point(number_of_point: int, dimension: int) -> list:
  points = []
  for _ in range(number_of_point):
    point = []
    for _ in range(dimension):
      point.append(round(random.uniform(0, 100), 3))
    points.append(Point(point))
  return points

def print_points(Points: list):
  for i in range (len(Points)):
    Points[i].print_point()

