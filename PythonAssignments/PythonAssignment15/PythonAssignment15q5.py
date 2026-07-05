from functools import reduce

def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))

    Maximum = reduce(lambda No1, No2: No1 if No1 > No2 else No2, Data)

    print("Original List :", Data)
    print("Maximum element :", Maximum)

if __name__ == "__main__":
    main()