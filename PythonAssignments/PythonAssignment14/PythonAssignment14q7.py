def main():
    ChkDivisible = lambda No: No % 5 == 0

    Value = int(input("Enter a number: "))

    Result = ChkDivisible(Value)

    print(Result)

if __name__ == "__main__":
    main()