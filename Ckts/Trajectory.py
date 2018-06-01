import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# x' =
# v' = k/m*(x-x0)^2

def step(x, center=0):
    res = np.zeros_like(x)
    for i in range(len(x)):
        if x[i]-center>0:
            res[i] = 1
    return res

def fun(y, t, V=1, E=1, m=1, hbar = 1):
    psi, dpsi = y
    dpsidt = [dpsi, 2*m*(V-E)*psi/(hbar**2)]
    return dpsidt


dx = 0.01
x = np.arange(0, 10, dx)
k = 1
V = 50*(step(x, 4.9)-step(x, 5))
#V = 2*np.ones_like(x)
E = 0.5
m = 2
hbar = 1
psi = np.zeros_like(x)
psi0 = [8 ,0]
for pos in range(len(x)-1):
    psi[pos] = odeint(fun, psi0, [x[pos],x[pos+1]], args=(V[pos], E, m, hbar))[1,0]
    dpsi = odeint(fun, psi0, [x[pos],x[pos+1]], args=(V[pos], E, m, hbar))[1,1]
    print(odeint(fun, psi0, [x[pos],x[pos+1]], args=(V[pos], E, m, hbar)))
    psi0 = [psi[pos], dpsi]
normed_psi = psi/np.linalg.norm(psi)
plt.plot(x, 10*normed_psi**2, 'b', label ='Psi')
plt.plot(x, np.ones_like(x)*E, 'r', label='Energy')
plt.plot(x, V, 'g',label = 'Potential')
plt.ylim([-0.1,1])
plt.grid()
plt.legend()
plt.show()




