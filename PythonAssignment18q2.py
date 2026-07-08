def Maximum(Arr):
    Max = Arr[0]

    for i in Arr:
        if i > Max:
            Max = i

    return Max

def main():
    Number = int(input("Enter number of elements:\n"))

    Data = []

    print("Enter the elements:")

    for i in range(Number):
        Value = int(input())
        Data.append(Value)

    Ans = Maximum(Data)

    print("Maximum number is:", Ans)

if __name__ == "__main__":
    main()