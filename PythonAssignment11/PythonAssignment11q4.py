def Reverse(No):
    Rev = 0

    while No != 0:
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10

    print("Reverse of the number is:", Rev)

def main():
    Value = int(input("Enter the number: "))

    Reverse(Value)

if __name__ == "__main__":
    main()