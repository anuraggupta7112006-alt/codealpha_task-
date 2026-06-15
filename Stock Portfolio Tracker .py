import csv

def main():
    # 1. Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "NVDA": 450,
        "MSFT": 380,
        "AMZN": 145
    }
    
    portfolio = {}
    total_investment = 0
    
    print("--- Stock Portfolio Tracker ---")
    print(f"Available stocks in system: {', '.join(stock_prices.keys())}\n")
    
    # 2. User inputs stock names and quantity
    while True:
        stock_name = input("Enter stock symbol (or type 'done' to finish): ").strip().upper()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print(f"⚠️ Stock symbol '{stock_name}' not found. Please try again.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("⚠️ Quantity cannot be negative.")
                continue
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid integer for quantity.")
            continue
            
        # Add or update quantity in the portfolio
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    if not portfolio:
        print("\nYour portfolio is empty. Exiting program.")
        return

    # 3. Calculate and display total investment value
    print("\n" + "="*35)
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Total Value':<10}")
    print("="*35)
    
    report_data = []
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        stock_total = qty * price
        total_investment += stock_total
        
        print(f"{stock:<10}{qty:<10}${price:<9}${stock_total:<10}")
        report_data.append([stock, qty, price, stock_total])
        
    print("="*35)
    print(f"Total Portfolio Value: ${total_investment}")
    print("="*35)
    
    # 4. File handling (Save results as a CSV file)
    save_choice = input("\nWould you like to save this report to a CSV file? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = "portfolio_report.csv"
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write CSV Headers
                writer.writerow(["Stock Symbol", "Quantity", "Price Per Share", "Total Value"])
                # Write Data Rows
                writer.writerows(report_data)
                # Write Total Summary
                writer.writerow([])
                writer.writerow(["Total Portfolio Value", "", "", f"${total_investment}"])
                
            print(f"📊 Success! Portfolio report saved safely to '{filename}'.")
        except IOError:
            print("⚠️ An error occurred while saving the file.")

if __name__ == "__main__":
    main()