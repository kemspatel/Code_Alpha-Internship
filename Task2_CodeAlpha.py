import yfinance as yf
import pandas as pd

class PortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] <= 0:
                del self.portfolio[symbol]
        else:
            print("Stock not found in portfolio.")

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            stock_data = yf.Ticker(symbol).history(period="1d")
            stock_price = stock_data['Close'].iloc[-1]
            total_value += stock_price * quantity
        return total_value

    def track_portfolio(self):
        print("Your Portfolio:")
        print("Symbol\t\tQuantity\tCurrent Price")
        for symbol, quantity in self.portfolio.items():
            stock_data = yf.Ticker(symbol).history(period="1d")
            stock_price = stock_data['Close'].iloc[-1]
            print(f"{symbol}\t\t{quantity}\t\t{stock_price}")

# Example usage
if __name__ == "__main__":
    tracker = PortfolioTracker()
    tracker.add_stock("AAPL", 13)
    tracker.add_stock("MSFT", 9)
    tracker.add_stock("GOOG", 7)

    tracker.track_portfolio()

    print("\nPortfolio Value:", tracker.get_portfolio_value())
