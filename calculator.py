def calculate(a, b, operation):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")

    if operation == "+":
        return a + b
    else:
        raise ValueError("Use + only.")


def main():
    print("Python Calculator")
    print("Supported operation: +")
    print("Type 'exit' to quit.")

    while True:
        operation = input("Enter operation (+): ").strip()

        if operation.lower() == "exit":
            print("Goodbye!")
            break

        if operation != "+":
            print("Use + only.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculate(a, b, operation)
            print("Result:", result)
        except (ValueError, TypeError, ZeroDivisionError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
