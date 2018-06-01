import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
plt.ion()
figure = plt.figure()

ax1 = figure.add_subplot(211)
ax2 = figure.add_subplot(212, projection='3d')


sig = 10.0
r = 20
b = 8/3
dt = 0.01
nn = 10000
t = np.zeros(nn)
x = np.zeros(nn)
y = np.zeros(nn)
z = np.zeros(nn)

t[0] = 0.1
x[0] = 0.1
y[0] = 0.1
z[0] = 0.1

ax2.plot(x,y,z)
plt.show()
for i in range(nn-1):
    fx = sig*(y[i] - x[i])
    fy = -x[i]*z[i] + r*x[i] - y[i]
    fz = x[i]*y[i] - b*z[i];

    x[i+1] = x[i] + dt*fx;
    y[i+1] = y[i] + dt*fy;
    z[i+1] = z[i] + dt*fz;
    t[i+1] = t[i] + dt;


ax1.plot(t, x)
for i in range(len(t)):
    ax2.plot(x[0:i], y[0:i], z[0:i])
    ax2.set_xlim(-20,20)
    ax2.set_ylim(-20,20)
    ax2.set_zlim(-20,20)
    if plt.waitforbuttonpress(0.0001):
        plt.close()
        break
    plt.cla()






