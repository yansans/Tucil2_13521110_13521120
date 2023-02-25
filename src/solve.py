from point import *
from sort import *

def distance(p1, p2):
    return math.sqrt((p1.c[0] - p2.c[0])**2 + 
                     (p1.c[1]- p2.c[1])**2 + 
                     (p1.c[2] - p2.c[2])**2)

def solve_bruteForce(points: list):
    n = len(points)
    min = math.inf
    for i in range(n):
        for j in range(i+1, n):
            d = distance(points[i], points[j])
            if d < min:
                min = d
                result = (points[i], points[j])
    return result, min

# return (pair, distance)
def solve(points: list) -> tuple:
    n = len(points)

    if n < 2:
        return None, math.inf
    if n == 2:
        return points, distance(points[0], points[1])

    # Sort points berdasarkan x
    points.sort(key=lambda p: p.c[0])
    # quick_sort(points, 0)

    # Bagi menjadi dua bagian
    mid = n // 2
    left = points[:mid]
    right = points[mid:]

    # Cari pasangan terdekat di setiap bagian
    leftRes, leftDistance = solve(left)
    rightRes, rightDistance = solve(right)

    if rightDistance <= leftDistance:
      res = rightRes
      resDist = rightDistance
    else:
      res = leftRes
      resDist = leftDistance

    # Cari pasangan terdekat yang berada di strip
    strip = []
    for point in left:
        if point.c[0] >= points[mid].c[0] - resDist:
            strip.append(point)
    for point in right:
        if point.c[0] <= points[mid].c[0] + resDist:
            strip.append(point)

    strip.sort(key=lambda p: p.c[1])
    # quick_sort(points, 1)
    
    for i in range (len(strip)):
        for j in range(i + 1, len(strip)):
            if  (abs(strip[i].c[0] - strip[j].c[0]) > resDist) or (abs(strip[i].c[1] - strip[j].c[1]) > resDist) or (abs(strip[i].c[2] - strip[j].c[2]) > resDist):
                break
            min = distance(strip[i], strip[j])
            if min < resDist:
                res = (strip[i], strip[j])
                resDist = min

    return res, resDist