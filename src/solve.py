from point import *
from sort import *
from main import *
import globals

def euclidean_distance(p1: Point, p2: Point) -> float:
    globals.count += 1
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

def solve(points: list, sort: int) -> tuple:
    n = len(points)
    dim = points[0].d

    if n == 1:
        return None, math.inf
    if n < 3:
        return solve_bruteForce(points)

    # Sort points berdasarkan x
    if sort == 2:
        points = quicksort(points, 0)
    else:
        points = merge_sort(points, 0)

    # Bagi menjadi dua bagian
    mid = n // 2
    mid_point = points[mid]
    left = points[:mid]
    right = points[mid:]

    # Cari pasangan terdekat di setiap bagian
    leftRes, leftDistance = solve(left, sort)
    rightRes, rightDistance = solve(right, sort)

    resDist = min(leftDistance, rightDistance)

    if  rightDistance > leftDistance:
        res = leftRes
    else:
        res = rightRes

    # Cari pasangan terdekat yang berada di strip
    strip = []
    for point in left:
        if point.c[0] >= mid_point.c[0] - resDist:
            strip.append(point)
    for point in right:
        if point.c[0] <= mid_point.c[0] + resDist:
            strip.append(point)

    # Sort strip berdasarkan y
    if (len(strip) > 1 and dim > 1):
        if sort == 2:
            strip = quicksort(strip, 1)
        else:
            strip = merge_sort(strip, 1)

    # Cari jarak terdekat di strip
    for i in range (len(strip)):
        for j in range(i + 1, min(i + globals.max_point + 1, len(strip))):
            if check_coord(strip, i, j, resDist):
                break
            mind = euclidean_distance(strip[i], strip[j])
            if mind < resDist:
                res = (strip[i], strip[j])
                resDist = mind

    return res, resDist
