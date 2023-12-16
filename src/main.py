import numpy as np
from plot import plot_performance
from marketmaker import MarketMaker
from brownian import BrownianMotion


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
    
    # Plots
    plot_performance(t, s, r, r_a, r_b, q, np.array(pnls))