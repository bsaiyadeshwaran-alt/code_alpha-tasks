
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

# Store portfolio details
portfolio = []

total_investment = 0

print("===================================")
print("       STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Get number of stocks
n = int(input("\nHow many stocks do you want to enter? "))

# Get stock details
for i in range(n):

    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

        price = stock_prices[stock_name]

        investment = price * quantity

        total_investment += investment

        portfolio.append(
            (stock_name, quantity, price, investment)
        )

        print("Investment added successfully!")

    else:
        print("Stock not available!")

# Display portfolio
print("\n===================================")
print("          YOUR PORTFOLIO")
print("===================================")

for stock, quantity, price, investment in portfolio:
    print(stock, "| Quantity:", quantity,
          "| Price: $", price,
          "| Investment: $", investment)

print("-----------------------------------")
print("Total Investment: $", total_investment)

# Save portfolio to a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=======================\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Investment: ${investment}\n"
        )

    file.write("\nTotal Investment: $" + str(total_investment))

print("\nPortfolio saved successfully in portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")
