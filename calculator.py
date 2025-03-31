def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input properly
try:
    price = float(input("Enter original price: "))
    discount = float(input("Enter discount percentage: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

# Calculate and display
final_price = calculate_discount(price, discount)
print(f"Final price after discount: ${final_price:.2f}")