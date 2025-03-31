Price = 100
discount_percentage = 25
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
calculate_discount("2000, 30")
calculate_discount(2000, 10)
calculate_discount(2000, 20)
