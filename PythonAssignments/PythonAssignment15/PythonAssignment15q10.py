def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))

    EvenNumbers = list(filter(lambda No: No % 2 == 0, Data))

    Count = len(EvenNumbers)

    print("Original List :", Data)
    print("Count of even numbers :", Count)

if __name__ == "__main__":
    main()