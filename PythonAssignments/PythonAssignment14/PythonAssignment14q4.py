def main():
    ChkEven = lambda No: True if No % 2 == 0 else False

    Value = int(input("Enter a number: "))

    Result = ChkEven(Value)

    print(Result)

if __name__ == "__main__":
    main()