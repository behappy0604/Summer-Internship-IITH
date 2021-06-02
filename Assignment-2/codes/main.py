import numpy as np
import matplotlib.pyplot as plt
M, O, R, E = (0, 0), (6, 0), (7.16, 4.35), (3.67, 6.36)


def line_gen(C1, C2):
    return ((C1[0], C2[0]), (C1[1], C2[1]))


l1 = line_gen(M, O)
l2 = line_gen(O, R)
l3 = line_gen(R, E)
l4 = line_gen(E, M)
l5 = line_gen(R, M)


def drawLine(line):
    plt.plot(line[0], line[1])
    
def drawVertix(coordinate, name):
    plt.plot(coordinate[0], coordinate[1], 'o')
    plt.text(coordinate[0] * (1 + 0.1), coordinate[1] * (1 - 0.1) , name)


# drawing Quadrilateral
drawLine(l1)
drawLine(l2)
drawLine(l3)
drawLine(l4)
drawLine(l5)

# plotting vertices
drawVertix(M, "M")
drawVertix(O, "O")
drawVertix(R, "R")
drawVertix(E, "E")


plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Quadrilateral')
plt.grid()
plt.show()

