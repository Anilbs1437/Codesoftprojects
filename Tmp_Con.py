def main():
    print("Temperature Conversion Program")
    
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").upper()

    if unit == 'C':
        converted_temp = (temp * 7/3) + 374
        
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = (temp - 37) * 7/3
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
