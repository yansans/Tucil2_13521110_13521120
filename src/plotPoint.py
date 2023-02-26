import matplotlib.pyplot as plt

def plotPoint(points: list, result: list, d: int):

    fig = plt.figure()
    if d == 1:
        for point in points:
            if (point == result[0] or point == result[1]):
                plt.scatter(point.c[0], 0, c = 'r')
            else :
                plt.scatter(point.c[0], 0, c = 'b')
    
    elif d == 2:
        for point in points:
            if (point == result[0] or point == result[1]):
                plt.scatter(point.c[0], point.c[1], c = 'r')
                plt.text(point.c[0], point.c[1], f"{point.c[0]}, {point.c[1]}", color='k')
            else :
                plt.scatter(point.c[0], point.c[1], c = 'b')
    
    elif d == 3:
        ax = fig.add_subplot(111, projection='3d')
        for point in points:
            if (point == result[0] or point == result[1]):
                ax.scatter(point.c[0], point.c[1], point.c[2], c = 'r')
                ax.text(point.c[0], point.c[1], point.c[2], f"{point.c[0]}, {point.c[1]}, {point.c[2]}", color='k')
            else :
                ax.scatter(point.c[0], point.c[1], point.c[2], c = 'b')

    elif d == 4:
        x = []
        y = []
        z = []
        c = []
        for point in points:
            x.append(point.c[0])
            y.append(point.c[1])
            z.append(point.c[2])
            c.append(point.c[3])
            
        ax = fig.add_subplot(111, projection='3d')
        img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
        for i in range(len(points)):
            for j in range (len(result)):
                if result[j].c[0] == x[i] and result[j].c[1] == y[i] and result[j].c[2] == z[i] and result[j].c[3] == c[i]:
                    ax.text(x[i], y[i], z[i], f"{x[i]}, {y[i]}, {z[i]}, {c[i]}", color='k')
        fig.colorbar(img)

    if d <= 4:
        plt.show()
    else :
        print("\n*Tidak bisa plot dimensi lebih dari 4")
