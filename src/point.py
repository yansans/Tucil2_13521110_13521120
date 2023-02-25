import math
import random

class Point:
    def __init__(self, coords: list):
        self.c = coords

    def print_point(self):
        print(f"({self.c[0]}, {self.c[1]}, {self.c[2]})")

def genereate_points(n: int) -> list:
  points = []
  for i in range(n):
    points.append(Point([random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]))
  return points

def print_points(Points: list):
  for i in range (len(Points)):
    print(f"{i+1}.", end = " ")
    Points[i].print_point()

