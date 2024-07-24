import re

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_pattern, email))

def main():
    
    emails = [
        "anil22222@gmail.com",
        "sunil.2003@sunil.101.com",
        "rajesh_kumar@tech.co.in",
        "manoj-raj.com",
        "vinay@20202",
        "siddarth@3032..com"
    ]
    
    print("Email Validation Results:")
    for email in emails:
        print(f"{email}: {is_valid_email(email)}")
    
    try:
        temp = float(input("Enter the temperature value: "))
        print(f"The entered temperature is: {temp}")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()
