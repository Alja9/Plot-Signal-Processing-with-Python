import numpy as np
from matplotlib import pyplot as plt

n = np.arange(0,10)
xN = 10*np.sin(2*np.pi*(10/100)*n)

plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Sinusoidal signal of discrete time')
plt.stem(n,xN, '-.')
plt.show()
