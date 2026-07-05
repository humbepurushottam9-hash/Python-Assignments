def main():
    Cube = lambda No: No ** 3

    Value = int(input("Enter a number: "))

    Result = Cube(Value)

    print("Cube is:", Result)

if __name__ == "__main__":
    main()