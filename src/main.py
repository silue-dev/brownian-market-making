import numpy as np
from plot import plot_performance
from marketmaker import MarketMaker
from brownian import BrownianMotion
from database import Database

def store_brownian_motions(db, n_sim: int) -> None:
    """"
    Generate a given number of Brownian motions and store them.

    Arguments
    ---------
    db    :  The database to store the brownian motions in.
    n_sim :  The number of Brownian motions to generate.

    """
    for _ in range(n_sim):
        bm = BrownianMotion(s0=100, n=200, dt=0.005, mu=0, sigma=2)
        serialized_bm = bm.serialize()
        db.insert_brownian_motion(serialized_bm)

def run_simulations(db: Database) -> list[np.ndarray]:
    """
    Run the market making simulation on the Brownian motions stored
    inside the given database.

    Arguments
    ---------
    db :  The database that contains the Brownian motions.

    Returns
    -------
    self.t    :  The array of time steps.
    self.bm.s :  The stock price movement (Brownian motion).
    r         :  The array containing reserve prices at each time step.
    r_a       :  The array of ask prices at each time step.
    r_b       :  The array of bid prices at each time step.
    q         :  The array of inventory snapshots at each time step.
    pnls      :  The PnL array, i.e., the PnL at each time step.

    """
    pnls = []
    brownian_motions = db.fetch_all_brownian_motions()
    for serialized_bm in brownian_motions:
        bm = BrownianMotion.deserialize(serialized_bm[0])
        marketmaker = MarketMaker(bm=bm, k=1.5, gamma=0.1)
        t, s, r, r_a, r_b, q, pnl = marketmaker.run()
        pnls.append(pnl)
    return t, s, r, r_a, r_b, q, np.array(pnls)

def main() -> None:
    """
    Main execution, which brings together the database setup, stock price
    data generation, market making simulation, and performance plotting.

    """
    # Setup database
    db = Database()
    db.connect()
    db.create_table()

    # Generate and store Brownian motions
    n_sim = 100
    store_brownian_motions(db, n_sim)

    # Run simulations
    t, s, r, r_a, r_b, q, pnls = run_simulations(db)
    
    # Clear and close databse
    db.clear()
    db.close()

    # Plot market maker's performance
    plot_performance(t, s, r, r_a, r_b, q, pnls)


if __name__ == '__main__':
    main()
