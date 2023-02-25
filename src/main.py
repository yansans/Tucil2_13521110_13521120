from point import *
from solve import *
from array import *
from plot3d import *
import time

if __name__ == '__main__':
    points = genereate_points(128)
    # print_points(points)
    
    print(f"Result with divide and conquer:")
    start_time = time.time()
    dnc, dncDist =solve(points)
    end_time = time.time()
    print(((end_time - start_time) * 10**3), "ms")
    dnc[0].print_point()
    dnc[1].print_point()
    print(f"Distance {dncDist}")

    print(f"\n\nResult with brute force:")
    start_time2 = time.time()
    brute, bruteDist = solve_bruteForce(points)
    end_time2 = time.time()
    print(((end_time2 - start_time2) * 10**3), "ms")
    brute[0].print_point()
    brute[1].print_point()
    print(f"Distance {bruteDist}")

    plot3d(points,dnc)
