def apply_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    
    return max(final_price, 0.0)  


print(apply_discount(100, 20))     
print(apply_discount(100, 100))    
print(apply_discount(100, 110))    
print(apply_discount(0, 50))       
print(apply_discount(100, 0))      




