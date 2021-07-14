import numpy as np

simlen = int(1e6)
gaussian_var_U = np.random.normal(0, 1/2, simlen)
gaussian_var_V = np.random.normal(0, 1/3, simlen)

count = np.size([i for i in range(simlen) if 3*gaussian_var_V[i] >= 2*gaussian_var_U[i]])

probability = count/simlen

print("Simulated probability : ", probability)
print("Theoretical probability : 0.5")
