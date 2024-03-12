import numpy as np
import matplotlib.pyplot as plt
import pickle

class BrownianMotion:
    """
    Represents a stock price movement `s` as a Brownian motion (more specifically, 
    a Wiener process), for which the formula goes as follows:

        s(t + dt) = s(t) + N(0, sigma^2 * dt)

    Intuitively, this formula means the that next price tick s(t+dt) is simply 
    the current price tick s(t) plus a random move, dictated by a normal 
    distribution with std (standard deviation) sigma. The std in s can be 
    interpreted as the volatility of the simulated stock. The multiplication 
    with dt means that the size of the price move increases with the size of 
    a time step. This makes sense, as a longer time step dt implies the 
    potential for a larger price move during that time.

    In the context of a discrete approximation for computer simulation, 
    the formula becomes:

        s(t + dt) = s(t) + sigma * sqrt(dt) * epsilon
    
    where epsilon is a random sample from a standard normal distribution, N(0,1). 
    The intuition behind this is based on statistical theory: 

        Consider a constant c, and a random variable X with a variance y. 
        The variance of c * X is c^2 * y.
        
    In our case, we need a variance of sigma^2 * dt. So if our random variable 
    epsilon is sampled from N(0,1), then we need to multiply epsilon with 
    sigma * sqrt(dt).

    Finally, we add a drift coefficient mu that induces a price trend:
    
        s(t + dt) = s(t) + mu * dt + sigma * sqrt(dt) * epsilon
    

    Arguments
    ---------
    s0 (float):     The starting price of the stock.
    n (int):        The number of time steps to take.
    dt (float):     The time step.
    mu (float):     The drift of the stock.
    sigma (float):  The volatility of the stock.

    """
    def __init__(self, s0, n, dt, mu, sigma):
        self.s0 = s0
        self.n = n
        self.dt = dt
        self.mu = mu
        self.sigma = sigma
        self.s = self.generate_stock_prices()

    def generate_stock_prices(self):
        s = np.zeros(self.n)
        s[0] = self.s0

        # Generate the stock price path
        for i in range(1, self.n):
            epsilon = np.random.normal()
            s[i] = s[i-1] + self.mu * self.dt + self.sigma * np.sqrt(self.dt) * epsilon

        return s
    
    def serialize(self):
        return pickle.dumps(self)
    
    def deserialize(serialized_bm):
        return pickle.loads(serialized_bm)


if __name__ == '__main__':
    bm = BrownianMotion(s0=100, n=1000, dt=0.01, mu=0, sigma=2)
    plt.plot(bm.s)
    plt.show()