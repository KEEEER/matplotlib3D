from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
color = ['b','g','r','c','m']
R=[]
F=[]
M=[]
C=[]
if not R:
	with open("the-file-name.txt") as f:
	    for line in f:
	        if ',' in line:
		        r, f , m , c= line.split(",", 3)
		        R.append(float(r))
		        F.append(float(f))
		        M.append(float(m))
		        C.append(color[int(c)])
		        
ax.scatter(R, F, M, c=C, marker='.')	                         
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()