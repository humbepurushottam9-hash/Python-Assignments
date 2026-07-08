def Divisible(No):
    if No % 5 == 0:
        print("True")
    else:
        print("False")

def main():
    Value = int(input("Enter the number:\n"))

    Divisible(Value)


if __name__=="__main__":
    main()