import numpy as np
from matplotlib import pyplot as plt

n = np.arange(-1,6)
xN = np.array([0,1,2,3,4,5,0])
xN_1 = n+1
xN_11 = [None] * len(n)
x=0
for l in xN:
       if xN_1[x] == 0:
              xN_11[x] = 1
       elif xN_1[x] == 1:
              xN_11[x] = 2
       elif xN_1[x] == 2:
              xN_11[x] = 3
       elif xN_1[x] == 3:
              xN_11[x] = 4
       elif xN_1[x] == 4:
              xN_11[x] = 5
       else:
              xN_11[x] = 0
       x+=1

plt.xlabel('n')
plt.ylabel('x[n+1]')
plt.title('Discrete Time Signals')
plt.stem(n,xN_11)
plt.show()
