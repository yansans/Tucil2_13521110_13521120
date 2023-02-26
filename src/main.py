from point import *
from solve import *
from plotPoint import *
import globals
import time

def nearest_neighbour(points: list, key: str, sort: int = 0) -> tuple:
    if key == "dnc":
        print(f"Result with divide and conquer:")
    elif key == "brute":
        print(f"Result with brute force:")
    start_time = time.time()
    if key == "dnc":
        nn, nnDist = solve(points, sort) 
    elif key == "brute":
        nn, nnDist = solve_bruteForce(points)
    end_time = time.time()
    diff = end_time - start_time
    print(f"{diff * 10**3:0.9f} ms")
    print_points(nn)
    print(f"Distance: {nnDist:0.9f}")
    if key == "dnc":
        print(f"Number of euclidian operation: {globals.count}")
    return nn, nnDist



if __name__ == '__main__':
    d = 3
    n_point = 1000
    globals.initialize()

    # 1 merge sort
    # 2 quick sort
    # else python sort
    sort = 2

    points = random_point(n_point ,d)
    
    nn_dnc , nnDist_dnc = nearest_neighbour(points, "dnc", sort)

    print()

    nn_b , nnDist_b = nearest_neighbour(points, "brute")

    # plotPoint(points, nn_dnc, d)
