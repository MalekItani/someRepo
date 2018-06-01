import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# x' = v
# v' = x^2 - 2x

def fun(y, t):
    x, v = y
    dydt = [v, -x**5 + 6*x**3-8*x]
    return dydt

dt = 0.01
t = np.arange(0, 10, dt)
y01 = [2,0]
sol1 = odeint(fun, y01, t)[:,0]
plt.plot(t, sol1, 'r', label='Sol1')

y02 = [-np.sqrt(2),-1]
sol1 = odeint(fun, y02, t)[:,0]
plt.plot(t, sol1, 'b', label='Sol2')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.legend()
plt.grid()
plt.show()

