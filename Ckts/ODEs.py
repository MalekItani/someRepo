import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# i' = -(R/Li + q/LC)
# q' = i

def step(x, center=0):
    res = np.zeros_like(x)
    for i in range(len(x)):
        if x[i]-center>0:
            res[i] = 1
    return res

def Q(y, t, R=1, L=1, C=1):
    i, q = y
    dydt = [-(i*R/L + q/(L*C)), i]
    return dydt

dt = 0.01
t = np.arange(0, 15, dt)
#E = 5*np.sin(1.5*t)*(1-step(t, 4)) + 2*(step(t, 6) - step(t, 7))
R = 0.5
L = 1
C = 1
y = np.zeros_like(t)
y0 = [-3,0]
i, q = odeint(Q, y0, t, args=(R, L, C))[:,0], odeint(Q, y0, t, args=(R, L, C))[:,1]
V_c = q/C

plt.ylim([-6,6])
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.plot(t, V_c, 'b', label='Vc')
plt.plot(t, i, 'g', label='Vr')
#plt.plot(t, E, 'r', label='Vsrc')
plt.grid()
plt.legend()

plt.show()




