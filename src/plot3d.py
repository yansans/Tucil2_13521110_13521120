import matplotlib.pyplot as plt

def plot3d(points: list, result: float):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for point in points:
        if (point == result[0] or point == result[1]):
            ax.scatter(point.c[0], point.c[1], point.c[2], c = 'r')
            ax.text(point.c[0], point.c[1], point.c[2], f"{point.c[0]}, {point.c[1]}, {point.c[2]}", color='k')
        else :
            ax.scatter(point.c[0], point.c[1], point.c[2], c = 'b')
    plt.gcf().text(0.02, 0.5, f"({result[0].c[0]}, {result[0].c[1]}, {result[0].c[2]})")
    plt.gcf().text(0.02, 0.6, f"({result[1].c[0]}, {result[1].c[1]}, {result[1].c[2]})")
    plt.show()