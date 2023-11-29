import numpy as np
import matplotlib.pyplot as plt

PRICE = 1000
TIME = 1000
DT = 0.01
MU = 1e-4   # drift
VOL = 0.01  # baseline volatility

def volatility(t):
    """ Returns the volatility at time t """
    variability = 0.5 * VOL * np.sin(2*np.pi*t) * np.random.normal()
    sigma = VOL + variability
    return sigma

def brownian(s_0=1000, mu=MU, T=TIME, dt=DT):
    """ Returns a Geometric Brownian Motion (GBM) """
    N = int(T/dt)
    s = np.zeros(N)
    s[0] = s_0
    for i in range(1,N):
        # Get volatility
        sigma = volatility(i*dt)
        # Compute new price at time i
        s[i] = s[i-1] * (1 + mu*dt + sigma*np.sqrt(dt)*np.random.normal())
    return s