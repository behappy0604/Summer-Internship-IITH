import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

y = np.linspace(-5,5,100)
x=(y*y)/24
plt.plot(x,y,label='$y^2=24x$')
plt.xlabel('$x$')
plt.ylabel('$y$')

#Plotting directrix
#equation of directrix is given x=-2
P=np.array([-6,-11])
Q=np.array([-6,11])
A=line_gen(P,Q)
plt.plot(A[0,:],A[1,:],label='$directrix$')

#plotting focus
plt.plot(6,0,'o',label='$focus$')
plt.text(2.2,0.2,'F')
plt.legend(loc='best')
plt.grid()
plt.xlim([-7,7])



plt.show()