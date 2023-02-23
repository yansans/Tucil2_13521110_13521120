from point import *

if __name__ == '__main__':
    all = generate_points(16, 2)
    all.print_points()
    print(all.distance(0, 1))
