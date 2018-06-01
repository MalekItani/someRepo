import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import CustomPlot as cp

# t' = w
# w' =

def fun(y, t, m = 1, L=1):
    theta, omega, alpha = y
    dydt = [omega, -alpha-m*np.sin(theta), 0]
    return dydt

dt = 0.05
t = np.arange(0, 50, dt)
x0 = 5
y0 = 5
R = 3
x01 = [np.pi/3,0,0]
theta = odeint(fun, x01, t)[:,0]
y = y0-R*np.cos(theta)
x = x0-R*np.sin(theta)


plt.ion()
plt.show()
for i in range(len(t)):
    plt.plot(x[:i],y[:i])
    plt.plot([x0, x[i]], [y0, y[i]], 'r' ,marker='o')
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.grid()
    if plt.waitforbuttonpress(0.01):
        break
    plt.cla()

