def ChkGreater(No1,No2):
    if No1 > No2:
        print("Greater number is:\n",No1)
    else:
        print("Greater number is:\n",No2)    

def main():
    Value1 = int(input("Enter first number:\n"))
    Value2 = int(input("Enter second number: \n"))
    ChkGreater(Value1,Value2)

if __name__ == "__main__":
    main()

    