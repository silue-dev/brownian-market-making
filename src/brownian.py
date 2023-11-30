import numpy as np
import matplotlib.pyplot as plt


PRICE = 1000
TIME = 1000
DT = 0.01
MU = 1e-4   # drift
VOL = 0.01  # baseline volatility
VAR = 1     # variability coefficient


def volatility(t, variability_coeff):
    """ Returns the volatility at time t """
    variability = variability_coeff * 0.5*VOL * np.sin(2*np.pi*t)
    sigma = VOL + variability
    return sigma

def brownian(s_0=1000, mu=MU, T=TIME, dt=DT, variability_coeff=VAR):
    """ Returns a Geometric Brownian Motion (GBM) """
    N = int(T/dt)
    s = np.zeros(N)
    s[0] = s_0
    for i in range(1,N):
        # Get volatility
        sigma = volatility(i*dt, variability_coeff)
        # Compute new price at time i
        s[i] = s[i-1] * (1 + mu*dt + sigma*np.sqrt(dt)*np.random.normal())
    timesteps = np.linspace(0, TIME, int(TIME/DT))
    return s, timesteps


if __name__ == "__main__":
    stock_prices, timesteps = brownian()

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(timesteps, stock_prices, label='Simulated Stock Price')
    plt.title('Simulated Stock Price using a Geometric Brownian Motion', fontweight='bold')
    plt.xlabel('Time', fontweight='bold')
    plt.ylabel('Stock Price', fontweight='bold')
    plt.legend()
    plt.grid(True)
    plt.show()