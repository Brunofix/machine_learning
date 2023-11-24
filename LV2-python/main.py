import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,3,1])
y= np.array([1,2,2,1,1])
plt.plot(x, y, 'b', linewidth=1, marker=".", markersize=7)
plt.axis([0,4,-2,4])
plt.xlabel('x')
plt.ylabel('y os')
plt.title('Primjer')
plt.show()