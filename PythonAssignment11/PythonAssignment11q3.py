def SumDigits(No):
    Total = 0

    while No != 0:
        Digit = No % 10
        Total = Total + Digit
        No = No // 10

    print("Sum of digits is:", Total)

def main():
    Value = int(input("Enter the number: "))

    SumDigits(Value)

if __name__ == "__main__":
    main()