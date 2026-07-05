from functools import reduce

def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))

    Product = reduce(lambda No1, No2: No1 * No2, Data)

    print("Original List :", Data)
    print("Product of all elements :", Product)

if __name__ == "__main__":
    main()