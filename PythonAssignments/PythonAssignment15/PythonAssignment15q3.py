def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))

    OddNumbers = list(filter(lambda No: No % 2 != 0, Data))

    print("Original List :", Data)
    print("Odd Numbers   :", OddNumbers)

if __name__ == "__main__":
    main()