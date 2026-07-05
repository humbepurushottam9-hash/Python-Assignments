from functools import reduce

def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))

    Addition = reduce(lambda No1, No2: No1 + No2, Data)

    print("Original List :", Data)
    print("Addition of all elements :", Addition)

if __name__ == "__main__":
    main()