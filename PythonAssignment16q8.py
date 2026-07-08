def Print(No):
    for i in range(1, No +1):
        print("*", end =" ")


def main():
    Value = int(input("Enter number:\n"))

    Print(Value)


if __name__=="__main__":
    main()