from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
with open("the-file-name.txt") as f:
    for line in f:
        if ',' in line:
	        r, f , m = line.split(",", 2)
	        R = float(r)
	        F = float(f)
	        M = float(m)
	        ax.scatter(R, F, M, c='k', marker='.')                 
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()