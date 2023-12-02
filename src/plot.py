import matplotlib.pyplot as plt

def plot_performance(t, s, r, r_a, r_b, q, pnls):
    f = plt.figure(figsize=(24, 4))

    # Final run prices
    ax1 = f.add_subplot(1, 4, 1)
    plt.plot(t, s, color='black', label='Market price')
    plt.plot(t, r, color='blue', linestyle='dashed', label='Reservation price')
    plt.plot(t, r_a, color='red', linestyle='', marker='x', markersize='2', label='Ask price')
    plt.plot(t, r_b, color='green', linestyle='', marker='x', markersize='2', label='Bid price')
    plt.xlabel('Time', fontweight='bold')
    plt.ylabel('Price', fontweight='bold')
    plt.grid(True)
    plt.legend()
    ax1.set_title("Final Run Prices", fontweight='bold')

    # Final run PnL
    ax2 = f.add_subplot(1, 4, 2)
    plt.plot(t, pnls[-1], color='green', label='PnL')
    plt.xlabel('Time', fontweight='bold')
    plt.ylabel('PnL', fontweight='bold')
    plt.grid(True)
    plt.legend()
    ax2.set_title("Final Run PnL", fontweight='bold')

    # Final run inventory
    ax3 = f.add_subplot(1, 4, 3)
    plt.plot(t, q, color='blue', label='Stocks held')
    plt.xlabel('Time', fontweight='bold')
    plt.ylabel('Inventory', fontweight='bold')
    plt.grid(True)
    plt.legend()
    ax3.set_title("Final Run Inventory", fontweight='bold')

    # PnL distribution
    ax4 = f.add_subplot(1, 4, 4)
    plt.hist(pnls[:,-1])
    plt.xlabel('PnL', fontweight='bold')
    plt.ylabel('Frequency', fontweight='bold')
    ax4.set_title("PnL Distribution", fontweight='bold')
    xmin, xmax = plt.xlim()
    margin_width = (xmax - xmin) * 0.5
    plt.xlim(xmin - margin_width, xmax + margin_width)

    plt.show()
