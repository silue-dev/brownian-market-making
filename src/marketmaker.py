import numpy as np
from random import random
from brownian import BrownianMotion
from plot import plot_performance

class MarketMaker:
    """
    This class implements a simulation of a market maker based on the 
    Avellaneda-Stoikov High-Frequency Trading (HFT) model. The 
    Avellaneda-Stoikov model is a mathematical framework used in 
    quantitative finance to model the optimal strategy for a market 
    maker, considering factors like inventory, risk aversion, and 
    market impact.

    In this implementation, the market maker sets bid (r_b) and ask 
    (r_a) prices for a stock, with these prices being influenced by 
    the stock's reserve price (r), which is adjusted for the market 
    maker's current inventory (q) and a gamma parameter that 
    represents risk aversion. The spread between bid and ask prices 
    is determined by both the gamma and k parameters, where k 
    measures market impact.

    The stock price movements are simulated using a Brownian motion 
    model, characterized by parameters mu (drift) and sigma (volatility). 
    The market maker's performance is evaluated in terms of cash flow, 
    inventory, and profit and loss (PnL) over the simulation period.


    Arguments
    ---------
    bm (np.array):  The brownian motion, representing the stock price.
    k (float):      The market impact parameter.
    gamma (float):  The risk aversion parameter.

    """
    def __init__(self, bm, k, gamma):
        self.bm = bm
        self.k = k
        self.gamma = gamma

        # Time steps
        self.t = np.linspace(0.0, bm.n * bm.dt, bm.n)
        
        # Order execution probability factors
        self.M = 1
        self.A = 1.0 / bm.dt / np.exp(k * self.M / 2)

    def run(self):
        # Trading time
        T = self.bm.n * self.bm.dt

        # Cash
        cash = np.empty(self.bm.n)
        cash[0] = 0

        # Inventory
        q = np.empty(self.bm.n)
        q[0] = 0

        # PnL
        pnl = np.empty(self.bm.n)
        pnl[0] = 0

        # Reserve price and quotes
        r = np.empty(self.bm.n)
        r_a = np.empty(self.bm.n)
        r_b = np.empty(self.bm.n)
        
        # Run market maker on stock
        for i in range(self.bm.n):
            # Compute reserve price and spread
            r[i] = self.bm.s[i] - q[i] * self.gamma * self.bm.sigma**2 * (T - self.bm.dt * i)
            spread = 2 / self.gamma * np.log(1 + self.gamma / self.k)

            # Compute quotes
            r_a[i] = r[i] + spread / 2
            r_b[i] = r[i] - spread / 2

            if i < self.bm.n - 1:
                # Since we don't have an order book, we must compute 
                # the probability that the asks and/or bids get executed:
                ### Deltas
                delta_a = r_a[i] - self.bm.s[i]
                delta_b = self.bm.s[i] - r_b[i]
                ### Intensities
                lambda_a = self.A * np.exp(-self.k * delta_a)
                lambda_b = self.A * np.exp(-self.k * delta_b)
                ### Order execution probabilities
                p_exec_a = 1 - np.exp(-lambda_a * self.bm.dt)
                p_exec_b = 1 - np.exp(-lambda_b * self.bm.dt)

                # We execute one order if a side gets hit
                executed_a = 0
                executed_b = 0
                if random() < p_exec_a:
                    executed_a = 1
                if random() < p_exec_b:
                    executed_b = 1

                # Compute inventory, cash, and PnL
                q[i+1] = q[i] - executed_a + executed_b
                cash[i+1] = cash[i] + r_a[i] * executed_a - r_b[i] * executed_b
                pnl[i+1] = cash[i+1] + q[i+1] * self.bm.s[i]
        
        return self.t, self.bm.s, r, r_a, r_b, q, pnl


if __name__ == "__main__":
    pnls = []
    n_sim = 100
    for i in range(n_sim):
        bm = BrownianMotion(s0=100,
                        n=200,
                        dt=0.005,
                        mu=0,
                        sigma=2)
        marketmaker = MarketMaker(bm=bm, k=1.5, gamma=0.1)
        t, s, r, r_a, r_b, q, pnl = marketmaker.run()
        pnls.append(pnl)
    
    plot_performance(t, s, r, r_a, r_b, q, np.array(pnls))