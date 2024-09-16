def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def modulus(x, y):
    return x % y

# Get input numbers function
def get_numbers():
    number1 = float(input("Please enter first number : "))
    number2 = float(input("Please enter second number : "))
    return number1, number2

def calculator():
    print("Select operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4', '5']:
            try:
                number1, number2 = get_numbers()
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            # Perform the corresponding operation
            if choice == "1":
                result = add(number1, number2)
                print("{} + {} = {}".format(number1, number2, result))
            elif choice == "2":
                result = subtract(number1, number2)
                print("{} - {} = {}".format(number1, number2, result))
            elif choice == "3":
                result = multiply(number1, number2)
                print("{} * {} = {}".format(number1, number2, result))
            elif choice == "4":
                result = divide(number1, number2)
                if result == "Error! Division by zero is not allowed.":
                    print(result)
                else:
                    print("{} / {} = {}".format(number1, number2, result))
            elif choice == "5":
                result = modulus(number1, number2)
                print("{} % {} = {}".format(number1, number2, result))

        else:
            print("Invalid input. Please select a valid operation.")

        calculator_off = input("Do you want to perform another calculation? (yes/no): ")
        if calculator_off.lower() != "yes":
            print("Exiting the calculator.....")
            break

calculator()




