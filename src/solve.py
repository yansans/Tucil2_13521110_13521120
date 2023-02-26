from point import *
from sort import *

def euclidean_distance(p1: Point, p2: Point) -> float:
    return math.sqrt(sum([(p1.c[i] - p2.c[i])**2 for i in range(p1.d)]))

def check_coord(points: list, i: int, j:int, dist: int) -> bool:
    for d in range (points[0].d):
        if abs(points[i].c[d] - points[j].c[d]) > dist:
            return True
    return False

def solve_bruteForce(points: list):
    n = len(points)
    min = math.inf
    for i in range(n):
        for j in range(i+1, n):
            d = euclidean_distance(points[i], points[j])
            if d < min:
                min = d
                result = (points[i], points[j])
    return result, min

def solve(points: list, sort: int = 0) -> tuple:
    n = len(points)

    if n <= 3:
        return solve_bruteForce(points)

    # Sort points berdasarkan x
    if sort == 1:
        points = merge_sort(points, 0)
    elif sort == 2:
        points = quicksort(points, 0)
    else:
        points.sort(key=lambda p: p.c[0])


    # Bagi menjadi dua bagian
    mid = n // 2
    mid_point = points[mid]
    left = points[:mid]
    right = points[mid:]

    # Cari pasangan terdekat di setiap bagian
    leftRes, leftDistance = solve(left, sort)
    rightRes, rightDistance = solve(right, sort)

    if rightDistance <= leftDistance:
      res = rightRes
      resDist = rightDistance
    else:
      res = leftRes
      resDist = leftDistance

    # Cari pasangan terdekat yang berada di strip
    strip = []
    for point in left:
        if point.c[0] >= mid_point.c[0] - resDist:
            strip.append(point)
    for point in right:
        if point.c[0] <= mid_point.c[0] + resDist:
            strip.append(point)

    # Sort strip berdasarkan y
    if (len(strip) > 1 and points[0].d > 1):
        if sort == 1:
            strip = merge_sort(strip, 1)
        elif sort == 2:
            strip = quicksort(strip, 1)
        else:
            strip.sort(key=lambda p: p.c[1])
    
    for i in range (len(strip)):
        for j in range(i + 1, len(strip)):
            # if  (abs(strip[i].c[0] - strip[j].c[0]) > resDist) or (abs(strip[i].c[1] - strip[j].c[1]) > resDist) or (abs(strip[i].c[2] - strip[j].c[2]) > resDist):
            if check_coord(strip, i, j, resDist):
                break
            min = euclidean_distance(strip[i], strip[j])
            if min < resDist:
                res = (strip[i], strip[j])
                resDist = min

    return res, resDist
