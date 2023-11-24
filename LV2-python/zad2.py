import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1, 2, 3, 4, 5, 6), delimiter=",", skiprows=1)
plt.scatter(data[:,3], data[:,0])
plt.xlabel("Snaga")
plt.ylabel("potrosnja")
plt.show()

sizes= 100 * data[:, 5] /np.max(data[:,5])
plt.scatter(data[:,3],data[:,0], s=sizes)
plt.show()