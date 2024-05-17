import numpy as np
import matplotlib.pyplot as plt

def plot_performance(t: np.ndarray, 
                     s: np.ndarray, 
                     r: np.ndarray, 
                     r_a: np.ndarray, 
                     r_b: np.ndarray, 
                     q: np.ndarray, 
                     pnls: np.ndarray) -> None:
    """
    Plots the performance of the market maker.

    Arguments
    ---------
    t    :  The array of time steps.
    s    :  The stock price movement (Brownian motion).
    r    :  The array containing reserve prices at each time step.
    r_a  :  The array of ask prices at each time step.
    r_b  :  The array of bid prices at each time step.
    q    :  The array of inventory snapshots at each time step.
    pnls :  The PnL arrays of all simulated runs.

    """
    f = plt.figure(figsize=(12, 12))

    # Final run prices
    ax1 = f.add_subplot(2, 2, 1)
    plt.plot(t, s, color='black', label='Market price')
    plt.plot(t, r, color='blue', linestyle='dashed', label='Reservation price')
    plt.plot(t, r_a, color='red', linestyle='', marker='x', markersize='2', 
             label='Ask price')
    plt.plot(t, r_b, color='green', linestyle='', marker='x', markersize='2', 
             label='Bid price')
    plt.xlabel('Time', fontweight='bold')
    plt.ylabel('Price', fontweight='bold')
    plt.grid(True)
    plt.legend()
    ax1.set_title("Final Run Prices", fontweight='bold')

    # Final run PnL
    ax2 = f.add_subplot(2, 2, 2)
    plt.plot(t, pnls[-1], color='green', label='PnL')
    plt.xlabel('Time', fontweight='bold')
    plt.ylabel('PnL', fontweight='bold')
    plt.grid(True)
    plt.legend()
    ax2.set_title("Final Run PnL", fontweight='bold')

    # Final run inventory
    ax3 = f.add_subplot(2, 2, 3)
    plt.plot(t, q, color='blue', label='Stocks held')
    plt.xlabel('Time', fontweight='bold')
    plt.ylabel('Inventory', fontweight='bold')
    plt.grid(True)
    plt.legend()
    ax3.set_title("Final Run Inventory", fontweight='bold')

    # PnL distribution
    ax4 = f.add_subplot(2, 2, 4)
    plt.hist(pnls[:,-1])
    plt.xlabel('PnL', fontweight='bold')
    plt.ylabel('Frequency', fontweight='bold')
    ax4.set_title("PnL Distribution", fontweight='bold')
    xmin, xmax = plt.xlim()
    margin_width = (xmax - xmin) * 0.5
    plt.xlim(xmin - margin_width, xmax + margin_width)

    plt.show()
