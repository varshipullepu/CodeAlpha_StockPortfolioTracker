import yfinance as yf
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
    
    def add_stock(self, symbol, shares, purchase_price):
        # Add stock to the portfolio
        self.portfolio[symbol] = {
            'shares': shares,
            'purchase_price': purchase_price
        }
    
    def remove_stock(self, symbol):
        # Remove stock from the portfolio
        if symbol in self.portfolio:
            del self.portfolio[symbol]
        else:
            print(f"Stock {symbol} not in portfolio.")
    
    def get_stock_data(self, symbol):
        # Get real-time stock data using yfinance
        try:
            stock = yf.Ticker(symbol)
            stock_info = stock.history(period="1d")
            if not stock_info.empty:
                current_price = stock_info['Close'][0]
                return current_price
            else:
                print(f"No data available for {symbol}.")
                return None
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None
    
    def track_portfolio(self):
        total_value = 0
        print("\nPortfolio Summary:")
        for symbol, info in self.portfolio.items():
            current_price = self.get_stock_data(symbol)
            if current_price is not None:
                value = info['shares'] * current_price
                total_value += value
                profit_loss = (current_price - info['purchase_price']) * info['shares']
                print(f"{symbol} - Shares: {info['shares']}, Current Price: {current_price:.2f}, "
                      f"Value: {value:.2f}, P/L: {profit_loss:.2f}")
            else:
                print(f"Could not retrieve data for {symbol}. Skipping.")
        
        print(f"\nTotal Portfolio Value: {total_value:.2f}")

# Example Usage:
portfolio = StockPortfolio()

# Add stocks to portfolio
portfolio.add_stock("AAPL", 10, 150)  # 10 shares of AAPL bought at $150
portfolio.add_stock("TSLA", 5, 700)   # 5 shares of TSLA bought at $700

# Track performance
portfolio.track_portfolio()

# Remove a stock
portfolio.remove_stock("AAPL")

# Track again
portfolio.track_portfolio()
