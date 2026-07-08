def Display(No):
    Count = 0

    while No > 0:
        Digit = No % 10
        Count = Count + Digit
        No = No // 10

    print("Addition is:",Count)   


def main():
    Value = int(input("Enter the number:\n"))

    Display(Value)

if __name__ =="__main__":
    main()