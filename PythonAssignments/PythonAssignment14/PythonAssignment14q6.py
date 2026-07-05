def main():
    Minimum = lambda No1, No2: No1 if No1 < No2 else No2

    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))

    Result = Minimum(Value1, Value2)

    print("Minimum number is:", Result)

if __name__ == "__main__":
    main()