def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q


print("Select operation.")
print("A.ADD")
print("B.SUBTRACT")
print("C.MULTIPLY")
print("D.DIVIDE")

while True:
    choice = input("Please Enter your choice(A or B or C or D): ")


    if choice in ('A', 'B', 'C', 'D'):
        try:
            num1 = input("Please Enter the first number: ")
            num2 = input("Please Enter second the number: ")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'B':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'C':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'D':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")