def main():
    Multiplication = lambda No1, No2: No1 * No2

    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))

    Result = Multiplication(Value1, Value2)

    print("Multiplication is:", Result)

if __name__ == "__main__":
    main()