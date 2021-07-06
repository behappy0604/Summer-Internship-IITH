import numpy as np
import matplotlib.pyplot as plt
a = 3
b = 27**.5
y = np.linspace(-10, 10)
x  = a*np.sqrt((1 + y**2/b**2))

e = 2
f = (a*e, 0)
lr = 2*b*b/a
M = (a*e, lr/2)
N = (a*e, -lr/2)
def drawVertix(coordinate, name):
    plt.plot(coordinate[0], coordinate[1], 'o')
    plt.text(coordinate[0] * (1 + 0.1), coordinate[1] * (1 - 0.1) , name)
    
def line_gen(C1, C2):
    return ((C1[0], C2[0]), (C1[1], C2[1]))

def drawLine(line):
    plt.plot(line[0], line[1])

xStandardHyperLeft = np.vstack((-x,y))
xStandardHyperRight = np.vstack((x,y))

drawVertix(f, "F")
drawVertix((a, 0), "(a, 0)")
drawVertix((-a, 0), "(-a, 0)")
drawVertix((0, b), "(0, b)")
drawVertix((0, -b), "(0, -b)")

MN = line_gen(M, N)
drawLine(MN)

drawVertix(M, "M")
drawVertix(N, "N")

plt.plot(xStandardHyperLeft[0,:],xStandardHyperLeft[1,:],label='Standard hyperbola',color='g')
plt.plot(xStandardHyperRight[0,:],xStandardHyperRight[1,:],color='g')
plt.grid(10)
plt.axis('equal')
plt.show()