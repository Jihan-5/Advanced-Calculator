def divide():
    x = float(input("Enter numerator: "))
    y = float(input("Enter denominator: "))
    
    if y != 0:
        print(f"Result: {x / y}")
    else:
        print("Error: Division by zero.")
