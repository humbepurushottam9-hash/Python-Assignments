def main():
    Addition = lambda No1, No2: No1 + No2

    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))

    Result = Addition(Value1, Value2)

    print("Addition is:", Result)

if __name__ == "__main__":
    main()