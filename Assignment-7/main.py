from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid([-10,10], range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


#defining planes:  n.T * x = c 
n1 = np.array([10,6,-18]).reshape((3,1))
A =  np.array([1,0,0]).reshape((3,1))
c1 = 3

#corresponding z for planes
z = (c1-n1[0]*xx-n1[1]*yy)/(n1[2])

#plotting planes
Plane=ax.plot_surface(xx, yy, z,label="P", color='b',alpha=0.25)
Plane._facecolors2d=Plane._facecolors3d

#show plot
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid() # minor


# Open the drawing window 1, draw in 3D space
fig = plt.figure(1)
ax = fig.gca(projection='3d')
 
 # Give points (3, 4, -5) and (-2, 1, 4)
x = [3, -2]
y = [4, 1]
z = [-5, 4]
 
 # Connect the first two points in the array
figure = ax.plot(x, y, z, c='r')


#plt.show()