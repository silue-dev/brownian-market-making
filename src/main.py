from brownian import brownian


class MarketMaker:
    def __init__(self, spread=1, update_interval=4, max_inventory=100):
        self.spread = spread
        self.inventory = 0
        self.cash = 0
        self.max_inventory = max_inventory
        self.bid_price = None
        self.ask_price = None
        self.update_interval = update_interval
        self.current_step = 0

    def update_prices(self, market_price):
        """ Updates the bid and ask order prices of the market maker """
        # Adjust the theoretical price based on inventory
        inventory_factor = self.inventory / self.max_inventory
        shift = inventory_factor * self.spread / 2
        theoretical_price = market_price - shift

        # Update prices only at specified intervals
        if self.current_step % self.update_interval == 0:
            self.bid_price = theoretical_price - self.spread / 2
            self.ask_price = theoretical_price + self.spread / 2
        self.current_step += 1

    def execute_trade(self, market_price):
        """ Executes trades when the market price hits the bid or ask orders """
        if market_price <= self.bid_price and self.inventory < self.max_inventory:
            # Buy stock
            self.inventory += 1
            self.cash -= self.bid_price
        elif market_price >= self.ask_price and self.inventory > -self.max_inventory:
            # Sell stock
            self.inventory -= 1
            self.cash += self.ask_price

    def pnl(self, price):
        """ Returns the current unrealized PnL """
        return self.cash + price * self.inventory
    

if __name__ == '__main__':
    stock_prices, _ = brownian()
    market_maker = MarketMaker()

    for price in stock_prices:
        market_maker.update_prices(price)
        market_maker.execute_trade(price)
    
    print(f"PnL = {market_maker.pnl(price)}.")