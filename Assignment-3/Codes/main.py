import numpy as np
import matplotlib.pyplot as plt


def line_gen(C1, C2):
    return ((C1[0], C2[0]), (C1[1], C2[1]))

def drawLine(line):
    plt.plot(line[0], line[1])
    
def drawVertix(coordinate, name):
    plt.plot(coordinate[0], coordinate[1], 'o')
    plt.text(coordinate[0] * (1 + 0.1), coordinate[1] * (1 - 0.1) , name)

def drawCircle(center, r):
    c1 = r
    theta1 = np.linspace(0,2*np.pi,50)
    x1 = center[0] + c1*np.cos(theta1)
    y1 = center[1] + c1*np.sin(theta1)
    plt.plot(x1,y1,label='$circle with (r=2.5)$')



# co-ordinates

(A, B, C, E, P, D) = ((0, 6), (0, 0), (8, 0), (4, 0), (5.53, 3.69), (2.88, 3.84))


# generating lines 

l1 = line_gen(A, C)
l2 = line_gen(B, C)
l3 = line_gen(A, B)
l4 = line_gen(A, P)
l5 = line_gen(P, E)
l6 = line_gen(P, C)
l7 = line_gen(B, D)
l8 = line_gen(A, E)


# drawing lines  
drawLine(l1)
drawLine(l2)
drawLine(l3)
drawLine(l4)
drawLine(l5)
drawLine(l6)
drawLine(l7)
drawLine(l8)



# drawing vertex 
drawVertix(A, "A")
drawVertix(B, "B")
drawVertix(C, "C")
drawVertix(E, "E")
drawVertix(P, "P")
drawVertix(D, "D")


drawCircle(E, 4)

# 9639091262


plt.axis('equal')
plt.show()

