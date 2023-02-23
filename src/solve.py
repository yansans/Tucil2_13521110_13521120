from point import *

def printListCoord(points: list):
    for i in range(len(points)):
        points[i].print_point()

def three_points(points: list) -> float:
    # return closest distance between three points
    d = distance(points[0], points[1])
    d = min(d, distance(points[0], points[2]))
    d = min(d, distance(points[1], points[2]))
    return d

def solve_2d(points: list, n: int) -> float:

    if n == 2:
        return distance(points[0], points[1])
    elif n == 3:
        return three_points(points)
    
    mid = n // 2
    mid_point = points[mid]
    d = min(solve_2d(points[:mid], mid), solve_2d(points[mid:], n - mid))

    strip = []
    for i in range(n):
        if abs(get_n_coord(points[i], 0) - get_n_coord(mid_point, 0)) < d:
            strip.append(points[i])

    # strip.sort(key = lambda point: get_n_coord(point, 1))
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if get_n_coord(strip[j], 1) - get_n_coord(strip[i], 1) >= d:
                break
            d = min(d, distance(strip[i], strip[j]))
        
    return d


    
