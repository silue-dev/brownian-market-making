import numpy as np
import matplotlib.pyplot as plt


def brownian_motion(s0, n, dt, mu, sigma):
    """
    Returns a stock price movement as a Brownian motion (more specifically, 
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

    Returns
    -------
    s (np.array):   The Brownian motion, representing the stock price.
    
    """

    # Initialize the array of stock prices
    s = np.zeros(n)
    s[0] = s0

    # Generate the stock price path
    for i in range(1, n):
        epsilon = np.random.normal()
        s[i] = s[i-1] + mu * dt + sigma * np.sqrt(dt) * epsilon

    return s


if __name__ == "__main__":
    s = brownian_motion(s0=100, n=1000, dt=0.01, mu=0, sigma=2)
    plt.plot(s)
    plt.show()