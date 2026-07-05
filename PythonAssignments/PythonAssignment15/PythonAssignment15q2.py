def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))

    EvenNumbers = list(filter(lambda No: No % 2 == 0, Data))

    print("Original List :", Data)
    print("Even Numbers  :", EvenNumbers)

if __name__ == "__main__":
    main()