def is_palindrome(s):
    stack = []
    
    for char in s:
        stack.append(char)
    
    for char in s:
        if char != stack.pop():
            return False
    
    return True
string = "malayalam"
print(f"{string} is a palindrome: {is_palindrome(string)}")  # Output: True

string = "ANIL"
print(f"{string} is a palindrome: {is_palindrome(string)}")  # Output: False