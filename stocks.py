import csv

# Hardcoded stock prices
stock_prices = {

    "RELIANCE": 2800,
    "TCS": 3750,
    "INFY": 1450,
    "HDFCBANK": 1620,
    "ICICIBANK": 1085,
    "LT": 3720,
    "SBIN": 650,
    "ITC": 470,
    "HINDUNILVR": 2550,
    "AXISBANK": 1070,
    "KOTAKBANK": 1750,
    "BAJFINANCE": 7200,
    "MARUTI": 11100,
    "ULTRACEMCO": 9700,
    "SUNPHARMA": 1280,

}


# Collect user input
portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): \n").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Please try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("Quantity must be non-negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid number. Try again.")

# Calculation and display
total_investment = 0
print("\nYour Investment Summary:")
print("-" * 35)
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = quantity * price
    total_investment += value
    print(f"{stock}: {quantity} × ₹{price} = ₹{value}")
print("-" * 35)
print(f"Total Investment Value: ₹{total_investment}")

# Optionally save to file
save = input("\nWould you like to save this to a file? (yes/no): ").lower()
if save == "yes":
    file_type = input("Choose file type: txt or csv: ").lower()
    if file_type == "txt":
        with open("investment_summary.txt", "w") as f:
            f.write("Your Investment Summary:\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = quantity * price
                f.write(f"{stock}: {quantity} × ${price} = ${value}\n")
            f.write(f"Total Investment Value: ₹{total_investment}\n")
        print("Saved to investment_summary.txt")
    elif file_type == "csv":
        with open("investment_summary.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = quantity * price
                writer.writerow([stock, quantity, price, value])
            writer.writerow([])
            writer.writerow(["Total Investment Value", "", "", total_investment])
        print("Saved to investment_summary.csv")
    else:
        print("Unsupported file type. Nothing saved.")
