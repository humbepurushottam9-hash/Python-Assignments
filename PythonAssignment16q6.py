def ChkNumber(No):
    if No > 0:
        print("Positive number")
    elif No < 0:
        print("Negative number")
    else:
        print("Zero")    

def main():
    Value1 = int(input("Enter the number:\n"))

    ChkNumber(Value1)


if __name__=="__main__":
    main()