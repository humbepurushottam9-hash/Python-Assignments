def main():
    Square = lambda No: No * No

    Value = int(input("Enter a number: "))

    Result = Square(Value)

    print("Square is:", Result)

if __name__ == "__main__":
    main()