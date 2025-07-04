def sum_digits(n):
    
    if n < 0:
        print("Please enter a positive number.")
        return None

    total = 0
    for digit in str(n):  
        total += int(digit)  
    return total


print(sum_digits(123456))             
