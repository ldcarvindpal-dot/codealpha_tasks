# Task 2: Stock Portfolio Tracker
# Calculates total investment based on manually defined stock prices

# hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

def main():
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:")
    for stock in stock_prices:
        print(stock, "-", stock_prices[stock])

    portfolio = {}
    print("\nEnter stock symbol and quantity. Type 'done' to finish.")

    while True:
        symbol = input("\nStock symbol: ")
        symbol = symbol.upper()

        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print("Stock not found in list. Try again.")
            continue

        quantity = input("Quantity: ")
        quantity = int(quantity)

        portfolio[symbol] = quantity
        print("Added", quantity, "shares of", symbol)

    # calculate total investment
    total = 0
    print("\n--- Portfolio Summary ---")
    for symbol in portfolio:
        qty = portfolio[symbol]
        price = stock_prices[symbol]
        value = qty * price
        total = total + value
        print(symbol, ":", qty, "shares x", price, "=", value)

    print("\nTotal Investment Value:", total)

    save = input("\nSave this summary to a file? (y/n): ")
    if save.lower() == "y":
        file = open("portfolio_summary.txt", "w")
        file.write("Stock Portfolio Summary\n")
        for symbol in portfolio:
            qty = portfolio[symbol]
            price = stock_prices[symbol]
            value = qty * price
            file.write(symbol + ": " + str(qty) + " shares x " + str(price) + " = " + str(value) + "\n")
        file.write("Total Investment: " + str(total) + "\n")
        file.close()
        print("Saved to portfolio_summary.txt")


main()
