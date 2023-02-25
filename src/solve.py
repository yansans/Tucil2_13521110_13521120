from point import *

# def printListCoord(points: list):
#     for i in range(len(points)):
#         points[i].print_point()

# def three_points(points: list) -> tuple:
#     # return closest distance between three points
#     p = [points[0], points[1]]
#     d = distance(points[0], points[1])
#     for i in range(3):
#         for j in range(i + 1, 3):
#             if distance(points[i], points[j]) < d:
#                 d = distance(points[i], points[j])
#                 p = [points[i], points[j]]
#     return (d, p)


# def solve_2d(points: list, n: int) -> tuple:

#     p = []

#     if n == 2:
#         p = points
#         return (distance(points[0], points[1]), p)
#     elif n == 3:
#         return three_points(points)
    
#     mid = n // 2
#     mid_point = points[mid]
#     dl, pl = solve_2d(points[:mid], mid)
#     dr, pr = solve_2d(points[mid:], n - mid)

#     d, p = (dl, pl) if dl < dr else (dr, pr)
    
#     strip = []
#     for i in range(n):
#         if abs(get_n_coord(points[i], 0) - get_n_coord(mid_point, 0)) < d:
#             strip.append(points[i])

#     # strip.sort(key = lambda point: get_n_coord(point, 1))
#     for i in range(len(strip)):
#         for j in range(i + 1, len(strip)):
#             if get_n_coord(strip[j], 1) - get_n_coord(strip[i], 1) < d:
#                 nd = distance(strip[i], strip[j])
#                 if nd < d: 
#                     d = nd
#                     p = [strip[i], strip[j]]

#     return (d, p)

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

def solve_bruteForce(points):
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
def solve(points) -> tuple:
    n = len(points)

    if n < 2:
        return None, math.inf
    if n == 2:
        return points, distance(points[0], points[1])

    # Sort points berdasarkan x
    points.sort(key=lambda p: p.x)

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
        if point.x >= points[mid].x - resDist:
            strip.append(point)
    for point in right:
        if point.x <= points[mid].x + resDist:
            strip.append(point)

    strip.sort(key=lambda p: p.y)
    
    for i in range (len(strip)):
        for j in range(i + 1, len(strip)):
            if  (abs(strip[i].x - strip[j].x) > resDist) or (abs(strip[i].y - strip[j].y) > resDist) or (abs(strip[i].z - strip[j].z) > resDist):
                break
            min = distance(strip[i], strip[j])
            if min < resDist:
                res = (strip[i], strip[j])
                resDist = min

    return res, resDist