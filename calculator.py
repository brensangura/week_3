price = 1000
discount_percent = 31
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Discount Calculator")
    print("-------------------")
    
    original_price = get_positive_number("Enter the original price of the item: $")
    discount_percentage = get_positive_number("Enter the discount percentage: ")
    
    final_price = round(calculate_discount(original_price, discount_percentage), 2)
    
    if discount_percentage >= 20:
        print(f"\nApplied {discount_percentage}% discount")
        print(f"Original price: ${original_price:.2f}")
        print(f"Final price: ${final_price:.2f}")
        print(f"You saved: ${original_price - final_price:.2f}")
    else:
        print(f"\nNo discount applied (minimum 20% required)")
        print(f"Price remains: ${original_price:.2f}")

if __name__ == "__main__":
    main()