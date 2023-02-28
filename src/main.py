from point import *
from solve import *
from plotPoint import *
import globals
import time

def main():

    d = menu(1)
    n_point = menu(2)
    rounding = menu(3)
    # 1 Merge sort , 2 Quick sort
    sort = menu(4)

    bound = 10**3

    points = random_point(n_point , d, rounding, bound)

    print("==================================================================================")
    
    nn_dnc , nnDist_dnc = nearest_point(points, d, "dnc", sort)

    print()

    nn_b , nnDist_b = nearest_point(points, d, "brute")

    print("==================================================================================")
    visual = input("Do you want to visualize the result? (y/n): ")
    if visual == "y":
        plotPoint(points, nn_dnc, d)

def nearest_point(points: list, dim:int, key: str, sort:int = 1) -> tuple:
    globals.initialize(dim)
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

def menu(type : int) -> int:
    if type == 1:
        prompt = "Enter the dimension of the points: "
        minval = 2
        err = "Dimension must be greater than 0"
    elif type == 2:
        prompt = "Enter the number of points: "
        minval = 1
        err = "Number of points must be greater than 0"
    elif type == 3:
        prompt = "Enter the rounding of the points: "
        minval = 0
        err = "Rounding must be greater than 0"
    elif type == 4:
        prompt = "Enter the sorting method\n1. Merge sort(default) \n2. Quick sort\n :"
        minval = 1
        err = "Sorting method must be 1 or 2"
    while True:
            try:
                num = int(input(prompt))
                if num < minval:
                    print(err)
                    continue
                break
            except ValueError:
                print("Invalid input")
                continue
    return num


def animation():
    animation = [
    "[        ]",
    "[=       ]",
    "[==      ]",
    "[===     ]",
    "[====    ]",
    "[=====   ]",
    "[======  ]",
    "[======= ]",
    "[========]",
    ]
    i = 0
    for i in range(len(animation)):
        print(animation[i % len(animation)], end='\r')
        time.sleep(0.1)

def startscreen():
    animation()
    print("Welcome to the nearest point program")
    input("Press enter to continue...")

if __name__ == "__main__":
    startscreen()
    main()