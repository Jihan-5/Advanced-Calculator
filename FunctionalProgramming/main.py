from Add import add
from Subtract import subtract
from Multiply import multiply
from Divide import divide
from Power import power, sqrt
from Trignometric import sin, cos, tan
from Logarithmic import log_base10, log_base2
from Constants import show_constants

def main():
    print("\n--- Scientific Calculator ---")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power & Square Root")
        print("6. Trigonometry (sin, cos, tan)")
        print("7. Logarithm (base 10, base 2)")
        print("8. Mathematical Constants")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            power()
        elif choice == '6':
            angle = float(input("Enter angle in degrees: "))
            print(f"Sin: {sin(angle)}")
            print(f"Cos: {cos(angle)}")
            print(f"Tan: {tan(angle)}")
        elif choice == '7':
            log_base10()
            log_base2()
        elif choice == '8':
            show_constants()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
