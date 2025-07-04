def validate_password(password):
    
    if len(password) < 8:
        return False

    has_letter = False
    has_number = False

    
    for char in password:
        if char.isalpha():     
            has_letter = True
        if char.isdigit():     
            has_number = True

    
    if has_letter and has_number:
        return True
    else:
        return False


print(validate_password("akorede123@"))  
print(validate_password("muja2006"))     

# Example 2

def validate_password(password):
    
    if len(password) < 8:
        return False

    has_letter = False
    has_number = False

    
    for char in password:
        if char.isalpha():     
            has_letter = True
        if char.isdigit():     
            has_number = True

    
    if has_letter and has_number:
        return True
    else:
        return False


print(validate_password("pass123"))


def validate_password(password):
    
    if len(password) < 8:
        return False

    has_letter = False
    has_number = False

    
    for char in password:
        if char.isalpha():     
            has_letter = True
        if char.isdigit():     
            has_number = True

    
    if has_letter and has_number:
        return True
    else:
        return False


print(validate_password("abc"))