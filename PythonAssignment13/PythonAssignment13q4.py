def DisplayBinary(No):
    print("Binary equivalent is:", bin(No))


def main():
    Value = int(input("Enter the number:\n"))

    DisplayBinary(Value)


if __name__ == "__main__":
    main()