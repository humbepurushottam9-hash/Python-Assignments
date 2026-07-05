def main():
    ChkOdd = lambda No: No % 2 != 0

    Value = int(input("Enter a number: "))

    Result = ChkOdd(Value)

    print(Result)

if __name__ == "__main__":
    main()