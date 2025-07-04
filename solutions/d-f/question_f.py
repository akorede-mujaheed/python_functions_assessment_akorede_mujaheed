

# EXAMPLE 2

def is_Palindrome(word):

    left_hand_side = 0
    right_hand_side = len(word) - 1
    
    
    while right_hand_side >= left_hand_side:
        if not word[left_hand_side] == word[right_hand_side]:

            return False
        
        left_hand_side += 1
        right_hand_side -= 1
    
    return True

print(is_Palindrome('racecar'))


# EXAMPLE 3

def is_Palindrome(word):
    left_hand_side = 0
    right_hand_side = len(word) - 1
    
    while right_hand_side >= left_hand_side:
        if not word[left_hand_side] == word[right_hand_side]:
            return False
        
        left_hand_side += 1
        right_hand_side -= 1
    
    return True

print(is_Palindrome('python'))


