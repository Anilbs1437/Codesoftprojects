import re

def check_password_strength(password):
 
    length_pattern = r'.{8,}'
    uppercase_pattern = r'[A-Z]'
    lowercase_pattern = r'[a-z]'
    digit_pattern = r'\d'
    special_pattern = r'[!@#$%^&*()\-_=+{};:,<.>\\|/?\[\]\'\"`~]'

    is_length_valid = bool(re.match(length_pattern, password))
    has_uppercase = bool(re.search(uppercase_pattern, password))
    has_lowercase = bool(re.search(lowercase_pattern, password))
    has_digit = bool(re.search(digit_pattern, password))
    has_special = bool(re.search(special_pattern, password))
    
    if (is_length_valid and has_uppercase and has_lowercase and
        has_digit and has_special):
        return "Strong"
    elif (is_length_valid and has_uppercase and has_lowercase and
          has_digit):
        return "Moderate"
    else:
        return "Weak"

password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
