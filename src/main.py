from point import *
from solve import *
from plotPoint import *
import globals
import time

def nearest_neighbour(points: list, key: str, sort: int = 1) -> tuple:
    globals.initialize(d)
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
    print(f"Number of euclidian operation: {globals.count}")
    return nn, nnDist


if __name__ == '__main__':
    
    while True:
        try:
            d = int(input("Enter dimension: "))
            if d < 1:
                print("Dimension must be greater than 0")
                continue
            break
        except:
            print("Invalid input")

    while True:
        try:
            n_point = int(input("Enter number of point: "))
            if n_point < 2:
                print("Number of point must be greater than 1")
                continue
            break
        except:
            print("Invalid input")

    while True:
        try:
            rounding = int(input("Enter rounding (ketelitian angka di belakang koma): "))
            if rounding < 0:
                print("Rounding must be greater than 0")
                continue
            break
        except:
            print("Invalid input")
    
    # 1 merge sort
    # 2 quick sort
    # else python sort
    while True:
        try:
            sort = int(input("Enter sorting method (1: merge sort, 2: quick sort, else python sort): "))
            break
        except:
            print("Invalid input")

    print("==================================================================================")
    points = random_point(n_point ,d, rounding, 10)
    
    nn_dnc , nnDist_dnc = nearest_neighbour(points, "dnc", sort)

    print()

    nn_b , nnDist_b = nearest_neighbour(points, "brute")

    print("==================================================================================")
    visual = input("Do you want to visualize the result? (y/n): ")
    if visual == "y":
        plotPoint(points, nn_dnc, d)
