<<<<<<< HEAD
=======
Price = 100
discount_percentage = 25
>>>>>>> 5f1ad5235d504252ad53a135bbe5ca748761e96e
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
<<<<<<< HEAD
print(calculate_discount(1080, 10)) # 1080


=======
    
calculate_discount("2000, 30")
calculate_discount(2000, 10)
calculate_discount(2000, 20)
>>>>>>> 5f1ad5235d504252ad53a135bbe5ca748761e96e
