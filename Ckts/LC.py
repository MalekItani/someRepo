import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def step(x, center=0):
    res = np.zeros_like(x)
    for i in range(len(x)):
        if x[i]-center>0:
            res[i] = 1
    return res

def I_Inductor(y, t, E=4, R=1, L=1):
    # VL = Ldi/dt
    # VL = E-R*i
    dydt = (E - y*R)/(L)
    return dydt

dt = 0.01
t = np.arange(0, 15, dt)
E = 5*np.sin(t)
R = 1
L = 1
y = np.zeros_like(t)
y0 = 0
for i in range(len(t)-1):
    y[i] = odeint(I_Inductor, y0, [t[i],t[i+1]], args=(E[i], R, L))[1]
    y0 = y[i]
V_r = y*R
V_l = E - V_r

plt.ylim([-6,6])
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.plot(t, V_l, 'b', label='VL')
plt.plot(t, V_r, 'g', label='Vr')
#plt.plot(t, E, 'r', label='Vsrc')
plt.grid()
plt.legend()

plt.show()




