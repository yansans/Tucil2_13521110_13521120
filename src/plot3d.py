import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot3d(points, result):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for point in points:
        if (point == result[0] or point == result[1]):
            ax.scatter(point.x, point.y, point.z, c='r')
            ax.text(point.x, point.y, point.z, f"{point.x}, {point.y}, {point.z}", color='k')
        else :
            ax.scatter(point.x, point.y, point.z, c='b')
    plt.gcf().text(0.02, 0.5, f"({result[0].c[0]}, {result[0].c[1]}, {result[0].c[2]})")
    plt.gcf().text(0.02, 0.6, f"({result[1].c[0]}, {result[1].c[1]}, {result[1].c[2]})")
    plt.show()