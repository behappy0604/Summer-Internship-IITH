import matplotlib.pyplot as plt
import math

AB, A, B = 5, (85/180)*math.pi, (115/180)*math.pi

def drawTriangle(AB, A, B):
    # drawing AB line of 5cm
    plt.plot((0,5), (0,0))

    lineLength = 10;

    (x1, x2) = (0,lineLength * math.cos(A))
    (y1, y2) = (0,lineLength * math.sin(A))

    (x3, x4) = (5, 5-lineLength * math.cos(B))
    (y3, y4) = (0 , lineLength * math.sin(B)) 

    plt.plot((x1, x2), (y1, y2))
    plt.plot((x3, x4), (y3, y4))

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Triangle')
    plt.show()


drawTriangle(AB, A, B)

def isIntersecting(x1, x2, y1, y2, x3, x4, y3, y4):
    den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if(den == 0): return False 
    t = ((xs1[0] - xs2[0]) * (ys1[0] - y4) - (ys1[0] - ys1[0]) * (xs2[0] - x4)) / den
    u = -((xs1[0] - xs1[1]) * (ys1[0] - ys1[0]) - (ys1[0] - y2) * (xs1[0] - xs2[0])) / den
    if (not (t > 0 and t < 1 and u > 0)): return False
    return True


isIntersecting(x1, x2, y1, y2, x3, x4, y3, y4)

