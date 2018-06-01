import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import random

# t' = w
# w' =

def fun(y, t, r0=np.array([2, 2]), k = 1, m=1):
    x, y, vx, vy = y
    r = np.array([x,y])
    drdt = -k / m * (r0 - r) / np.linalg.norm(r0 - r) ** 3
    dydt = [vx , vy,drdt[0], drdt[1]]
    return dydt

dt = 0.05
t = np.arange(0, 4, dt)
r = np.zeros((len(t), len(t)))
v = np.zeros((len(t), len(t)))
k = 4
m = 1
R = 3
plt.ion()
plt.show()

random.seed(1453274233417)
for j in range(10):
    y0 = 4.5 + 0.1*j
    vx0 = 4
    vy0 = 0
    i0 = [0, y0, vx0, vy0]
    center = np.array([5, 5])
    x = odeint(fun, i0, t, args=(center, k, m))[:, 0]
    y = odeint(fun, i0, t, args=(center, k, m))[:, 1]
    for i in range(len(t)):
        plt.plot(x[:i],y[:i])
        plt.plot([i0[0], x[i]], [i0[1], y[i]], 'r' ,marker='o')
        plt.plot(center[0], center[1], 'g', marker = '+')
        plt.xlim([0, 10])
        plt.ylim([0, 10])
        plt.grid()
        if plt.waitforbuttonpress(0.01):
            break
        plt.cla()

