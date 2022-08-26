"""
importing numpy and matplotlib libery:
"""
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy import interpolate

"""
Control Points:
"""
w= np.array([[442,23],
            [418,69],
            [450,186],
            [429,332],
            [295,422],
            [0,523],
            [257,569],
            [306,580]])

def B_spline(waypoints):
    x = []
    y = []
    for point in waypoints:
        x.append(point[0])
        y.append(point[1])
    
    tck, rest = interpolate.splprep([x,y])
    u = np.linspace(0,1,num=100)
    smooth = interpolate.splev(u,tck)
    return smooth

x,y = B_spline(w)
z = np.zeros(len(x))
sf = []
for i in range(len(x)):
    sf.append([x[i], y[i], z[i]])
sf = np.array(sf)

def rot(theta):
    t = np.deg2rad(theta)                   #converting degree into rad
    rot = np.array([[np.cos(t), 0, np.sin(t)],
                    [0.        , 1,        0],
                   [-np.sin(t),0, np.cos(t)]])
    return rot

solid = []
for i in range(360):
    solid.append((sf@rot(i)))

fig, axes = plt.subplots(1, 2, constrained_layout=True,  figsize=(10,10))
ax = plt.axes(projection='3d')
for i in range (len(solid)):
    ax.scatter3D(solid[i].T[0],solid[i].T[1],solid[i].T[2], c='b', alpha=0.2);
plt.title('Wine Glass using B_spline curve')
plt.show()

