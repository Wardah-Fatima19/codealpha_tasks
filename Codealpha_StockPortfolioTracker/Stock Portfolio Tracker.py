def get_prices():
    return {
        "APPLE": 180,
        "TESLA": 250,
        "NVIDIA": 500,
        "META": 400,
        "NETFLIX": 350,
        "MICROSOFT": 550
    }

def main():
    prices = get_prices()
    portfolio = {}
    print("******* Stock Portfolio Tracker Started *******")

    while True:
        stock = input("\nEnter stock name (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in prices:
            print("\n Stock not available in list.")
            continue

        qty = int(input("\nEnter quantity: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    total = 0
    print("\nPortfolio Summary:")

    for stock in portfolio:
        value = portfolio[stock] * prices[stock]
        print(f"{stock} -> {portfolio[stock]} shares = ${value}")
        total += value

    print("\nTotal Investment Value =", total)

    save = input("\nSave to file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.txt", "w") as f:
            for stock in portfolio:
                f.write(f"{stock},{portfolio[stock]},{prices[stock]}\n")
            f.write(f"Total,{total}")
        print("\nData saved in portfolio.txt")


main()